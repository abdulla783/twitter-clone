from rest_framework import serializers
from users.models import Profile
from django.contrib.auth.models import User
from users.forms import UserRegisterForm


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'iput_type': 'password'}, write_only=True)
    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'password2', 'first_name', 'last_name',]
        extra_kwargs = {
                'password': {'write_only':True}
        }

    def save(self):
        account = User.objects.create(
            email = self.validated_data['email'],
            username = self.validated_data['username'],
            first_name = self.validated_data['first_name'],
            last_name = self.validated_data['last_name'],
            )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match'})
        account.set_password(password)
        account.save()
        return account