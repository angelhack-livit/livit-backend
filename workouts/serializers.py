from workout.models import Workout, TrainingSession
from rest_framework import serializers


class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout


class TrainingSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingSession