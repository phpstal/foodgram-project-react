from djoser.serializers import UserSerializer
from django.contrib.auth import get_user_model

User = get_user_model()


class CustomUserSerializer(UserSerializer):
    class Meta:
        model = User
        fields = '__all__' 