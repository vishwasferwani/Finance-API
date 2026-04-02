from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    #custom field in default django user model
    ROLE_CHOICES = (
        ('viewer', 'Viewer'),
        ('analyst', 'Analyst'),
        ('admin', 'Admin'),
    )

    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    is_active = models.BooleanField(default=True)