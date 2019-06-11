from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    USER_TYPE = (
        ("1", "Developer"),
        ("2", "Customer"),
    )
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE)

    def __str__(self):
        return self.username
