# from django.shortcuts import render
from rest_framework import viewsets
from app.models import User
from app.serializers import UserSerializer
# Create your views here.


class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
