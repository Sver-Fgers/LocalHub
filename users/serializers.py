from rest_framework import serializers
from .models import User
from allauth.account.models import EmailAddress

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["username", "email", "password"]

    def create(self, validated_data):
        user = User(
            username=validated_data["username"],
            email=validated_data.get("email", "")
        )
        user.set_password(validated_data["password"])
        user.save()

        # Add email into allauth’s EmailAddress model
        if user.email:
            EmailAddress.objects.create(
                user=user,
                email=user.email,
                primary=True,
                verified=False  # can set True if you don’t require verification
            )

        return user
