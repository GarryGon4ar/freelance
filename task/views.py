from django.db import transaction
from django.db.models import F
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from users.models import CustomUser
from .serializers import TaskSerializer
from .permissions import IsOwnerOrReadOnly
from .models import Task


class TaskList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        with transaction.atomic():
            CustomUser.objects.select_for_update().filter(pk=instance.owner.id).update(balance=F('balance') - instance.price)
            CustomUser.objects.select_for_update().filter(username=request.user.username).update(balance=F('balance') + instance.price)