from profiles.models import UserProfile, Trainer
from rest_framework import serializers
from taggit_serializer.serializers import (TagListSerializerField,
                                           TaggitSerializer)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('email', 'first_name', 'last_name', 'age', 'location',
        		  'bio', 'height', 'weight', 'image_url')


class TrainerSerializer(TaggitSerializer, serializers.ModelSerializer):
    expertise = TagListSerializerField()

    class Meta:
        model = Trainer
        fields = ("first_name", "last_name", "location", "expertise", "age", "email",
        		  "image_url")