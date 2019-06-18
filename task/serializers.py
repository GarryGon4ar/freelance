from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'owner', 'developer', 'title', 'description', 'award', 'finished', 'created_at',)
        read_only_fields = fields
