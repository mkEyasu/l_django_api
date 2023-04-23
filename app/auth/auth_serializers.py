from app.models import User
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.core.exceptions import ObjectDoesNotExist
from app.serializers import UserSerializer
from rest_framework_simplejwt.settings import api_settings
from django.contrib.auth.models import update_last_login


class AuthloginSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        # infos = UserSerializer(self.user).data

        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)

        if api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, self.user)
        return data


class AuthSignupSerializer(UserSerializer):
    email = serializers.EmailField(required=True, max_length=128, write_only=True)
    password = serializers.CharField(max_length=80, write_only=True, required=True, min_length=8)

    class Meta:
        model = User
        fields = ['id', 'email', 'password']
        extra_kwargs = {"password": {"write-only": True}}

    def create(self, validated_data):
        try:
            user = User.objects.get(email=validated_data['email'])
        except ObjectDoesNotExist:
            user = User.objects.create_user(**validated_data)
        return user
