from django.db import transaction
from django.db.models import F
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import generics, status
from rest_framework.response import Response

from users.models import CustomUser
from .serializers import TaskSerializer
from .permissions import IsOwnerOrReadOnly
from .models import Task

from django.contrib.auth import get_user_model


class TaskList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


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

        instance.developer = self.request.user
        instance.developer.balance = F('balance') + instance.award
        instance.developer.save()

        owner = instance.owner
        owner.balance = F('balance') - instance.award
        owner.save()

        return super().put(request, *args, **kwargs)

