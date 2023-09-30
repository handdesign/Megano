from rest_framework import serializers
from .models import Profile


class SignInSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)


class SignUpSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'user', 'fullName', 'email', 'phone', 'avatar']
        read_only_fields = ['id', 'user']
        extra_kwargs = {
            'fullName': {'required': False},
            'email': {'required': False},
            'phone': {'required': False},
            'avatar': {'required': False}
        }


class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    def validate_old_password(self, value):
        user = self.context['request'].user

        if not user.check_password(value):
            raise serializers.ValidationError("Invalid old password")
        return value
