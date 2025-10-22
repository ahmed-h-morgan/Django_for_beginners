from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class CustomUser(AbstractUser):        # new class inherited from AbstractUser to customize User_Accounts attributes for 
    age = models.PositiveIntegerField(null=True, blank=True)     # Add new customized user field to the User table
