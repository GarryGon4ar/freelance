from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    USER_TYPE = (
        ("developer", "Developer"),
        ("customer", "Customer"),
    )
    user_type = models.CharField(max_length=9, choices=USER_TYPE)
    balance = models.PositiveIntegerField(default=0)

