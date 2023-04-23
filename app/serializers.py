from rest_framework.serializers import HyperlinkedModelSerializer
from app.models import User

class UserSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ['url', 'sur_name', 'email', 'is_active']
        read_only_fields = ['is_active']