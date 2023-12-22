from rest_framework import serializers
from .models import Gym, Trainer, Client, WorkoutSession

class GymSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gym
        fields = ['id', 'name', 'address']

class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainer
        fields = ['id', 'name', 'specialization', 'gym']

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'name', 'age']
    
    def validate_age(self, value):
        if value < 0:
            raise serializers.ValidationError("Age must be a positive integer.")
        return value

class WorkoutSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutSession
        fields = ['id', 'client', 'trainer', 'date', 'duration']
        