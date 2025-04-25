from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    preferences = models.JSONField(default=dict)
    
    class Meta:
        db_table = 'auth_user'
