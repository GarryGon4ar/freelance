from _decimal import Decimal

from django.db import transaction
from django.db.models import F
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Task


class TaskSerializer(ModelSerializer):
    url = SerializerMethodField('get_task_url')
    class Meta:
        model = Task
        fields = ('id', 'owner', 'title', 'description', 'award', 'finished', 'created_at','url', )
        read_only_fields = ('owner', 'finished', 'created_at', 'url',)

    def get_task_url(self, task):
        request = self.context.get('request')
        task_url = str(task.id)
        return request.build_absolute_uri(task_url)

    def validate(self, data):
        with transaction.atomic():
            user = self.context['request'].user
            if data['award'] > user.balance:
                raise serializers.ValidationError("У вас недостаточно средств, чтобы создать таск.")
            elif user.balance < user.expenses + Decimal(data['award']):
                raise serializers.ValidationError("Пожалуйста пополните баланс или назначьте меньшую сумму за таск.")
            user.expenses = (F('expenses') + Decimal(data['award']))
            user.save()
            return data


class TaskDetailSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'owner', 'developer', 'title', 'description', 'award', 'finished', 'created_at',)
        read_only_fields = fields
