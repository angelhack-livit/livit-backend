from profiles.models import UserProfile, Trainer
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('email', 'first_name', 'last_name', 'age', 'location',
        		  'bio', 'height', 'weight')


class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainer
        fields = ('email', 'first_name', 'last_name', 'age', 'location',
        		  'bio',)