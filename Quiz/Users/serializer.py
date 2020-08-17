from rest_framework import serializers
from . import models
from .models import Users


class AddSerializer(serializers.ModelSerializer):
    class Meta:
        model=Users
        fields='__all__'

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model=Users
        fields=('id','Username','Password')
