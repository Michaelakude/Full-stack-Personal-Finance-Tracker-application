from rest_framework import serializers
from .models import *
from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model
User = get_user_model()

class UserCreateSerializer(UserCreateSerializer):
	class Meta(UserCreateSerializer.Meta):
		model = User
		fields = ('id', 'email', 'name', 'password')

class BankAccountSerialzer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = BankAccount
		fields = ['account_id','balance', 'name']
		