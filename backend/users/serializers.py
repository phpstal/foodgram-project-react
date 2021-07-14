from rest_framework import serializers

from .models import FoodUser


class FoodUserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'username',
            'password'
            'email',
            'first_name',
            'last_name',
        )
        model = FoodUser