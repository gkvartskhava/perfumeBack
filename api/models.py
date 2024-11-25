from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):

    ADMIN = 'admin'
    MANAGER = 'manager'
    CUSTOMER = 'customer'
    ROLE_CHOICES = [
        (ADMIN,'Administrator'),
        (MANAGER,'manager'),
        (CUSTOMER,'customer'),
    ]

    role = models.CharField(max_length=20, choices = ROLE_CHOICES, default = 'CUSTOMER')




