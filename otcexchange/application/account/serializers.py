from rest_framework import serializers
from django.contrib.auth import get_user_model



class UserRegisterSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = get_user_model()
        fields = ("phone_number", "password", "approve_rules")
        extra_kwargs = {
            'password': {'write_only': True, 'required': True},
        }
    