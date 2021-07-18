from djoser.serializers import UserCreateSerializer
from .models import CustomUser


class UserRegistrationSerializer(UserCreateSerializer):

    class Meta:
        model = CustomUser
        fields = '__all__'