from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Task


class TaskSerializer(ModelSerializer):
    url = SerializerMethodField('get_task_url')
    class Meta:
        model = Task
        fields = ('id', 'owner', 'title', 'description', 'award', 'finished', 'created_at','url', )
        read_only_fields = ('owner', 'finished', 'created_at', 'url')

    def get_task_url(self, task):
        request = self.context.get('request')
        task_url = str(task.id)
        return request.build_absolute_uri(task_url)


class TaskDetailSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'owner', 'developer', 'title', 'description', 'award', 'finished', 'created_at',)
        read_only_fields = fields
