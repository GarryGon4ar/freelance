from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    DEVELOPER = 0
    CUSTOMER = 1
    USER_TYPE = (
        (DEVELOPER, "Developer"),
        (CUSTOMER, "Customer"),
    )
    email = models.EmailField(verbose_name='email address',unique=True)
    user_type = models.IntegerField(choices=USER_TYPE)
    balance = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    expenses = models.DecimalField(default=0, max_digits=5, decimal_places=2)
