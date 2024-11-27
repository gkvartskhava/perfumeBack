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

class Category(models.Model):
    gender = models.CharField(max_length=100)
    
    def __str__(self):
        return self.gender


class PerfumeDetails(models.Model):
    name = models.CharField(max_length=900)
    description = models.TextField()
    image=models.CharField(max_length=10000)
    image2 = models.ImageField(upload_to="images/")
    price = models.IntegerField()
    quantity = models.IntegerField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name="sex")

    def __str__(self):
        return self.name



