from rest_framework import serializers
from .models import User, FavCharacter, FavQuote
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):
    """ Serializes our user data"""

    class Meta:
        model = User
        fields = '__all__'

    def validate(self, data):
        email_validation = 'email' in data and data['email']
        validate_password(password=data['password'].strip())
        errors = {}

        if not email_validation:
            errors['email'] = ['Invalid email']

        if len(errors):
            raise serializers.ValidationError(errors)

        # hash password
        data['password'] = make_password(data.get('password'))
        saved_data = {
            'username': data['username'],
            'email': data['email'],
            'password': data['password'],
            "is_admin": data.get("is_admin", False)
        }

        return saved_data


class FavCharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavCharacter
        fields = '__all__'


class FavQuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavQuote
        fields = '__all__'

