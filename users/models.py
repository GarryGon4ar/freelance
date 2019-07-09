from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    USER_TYPE = (
        ("developer", "Developer"),
        ("customer", "Customer"),
    )
    email = models.EmailField(verbose_name='email address',unique=True)
    user_type = models.CharField(max_length=9, choices=USER_TYPE)
    balance = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    expenses = models.DecimalField(default=0, max_digits=5, decimal_places=2)
