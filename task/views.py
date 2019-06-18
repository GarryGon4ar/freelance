from django.db import transaction
from django.db.models import F
from rest_framework import generics, status
from rest_framework.response import Response

from .serializers import TaskSerializer
from .models import Task


class TaskList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def post(self, request, *args, **kwargs):
        if self.request.user.user_type == 'developer':
            return Response({'detail': "Только заказчик может создавать заказ."},
                            status=status.HTTP_403_FORBIDDEN)
        else:
            return super().post(request, *args, **kwargs)


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    @transaction.atomic()
    def put(self, request, *args, **kwargs):
        instance = self.get_object()

        if instance.finished:
            return Response({'detail': "Заказ уже выполнен"},
                            status=status.HTTP_403_FORBIDDEN)

        if instance.owner.balance < instance.award:
            return Response({'detail': "У заказчика не достаточно денег не балансе"},
                            status=status.HTTP_403_FORBIDDEN)
        if self.request.user.user_type != 'customer':
            instance.developer = self.request.user
            instance.developer.balance = F('balance') + instance.award
            instance.finished = True
            instance.save()
            owner = instance.owner
            owner.balance = F('balance') - instance.award
            owner.save()
        else:
            return Response({'detail': "Заказчик не может выполнять задания"},
                            status=status.HTTP_403_FORBIDDEN)

        return super().put(request, *args, **kwargs)
