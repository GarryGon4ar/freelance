from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    developer = serializers.ReadOnlyField(source='developer.username')

    class Meta:
        model = Task
        fields = ['title', 'description', 'price', 'owner', 'developer', 'finished']
