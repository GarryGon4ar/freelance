from django.db import models
from users.models import CustomUser


class Task(models.Model):
    owner = models.ForeignKey(CustomUser, related_name='tasks', on_delete=models.CASCADE)
    developer = models.ForeignKey(CustomUser, related_name='Developer', on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    award = models.DecimalField(default=0, max_digits=5, decimal_places=2)
    finished = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.title}-{self.award}'