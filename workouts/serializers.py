from workouts.models import Workout, TrainingSession
from rest_framework import serializers
from profiles.serializers import UserSerializer
from profiles.serializers import TrainerSerializer


class WorkoutSerializer(serializers.ModelSerializer):

    class Meta:
        model = Workout


class SlugRelatedModuleField(serializers.SlugRelatedField):

    def get_queryset(self):
        queryset = self.queryset
        return queryset


class TrainingSessionSerializer(serializers.ModelSerializer):
    users_count = serializers.SerializerMethodField()
    users = UserSerializer(many=True, read_only=True)
    trainer = TrainerSerializer()
    workouts = WorkoutSerializer(many=True, read_only=True)

    @staticmethod
    def get_users_count(instance):
        return instance.users.all().count()

    class Meta:
        model = TrainingSession
        fields = ("pk", "name", "description", "start_date", "end_date", "trainer",
                  "users", "back_ground_image", "users_count", "workouts")