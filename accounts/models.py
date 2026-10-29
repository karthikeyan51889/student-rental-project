from django.contrib.auth.models import AbstractUser
from django.db import models
class User(AbstractUser):
 class Role(models.TextChoices):
  OWNER='owner','Owner'
  STUDENT='student','Student'
 role=models.CharField(max_length=10,choices=Role.choices,default=Role.STUDENT)
 phone=models.CharField(max_length=20,blank=True)
 def __str__(self): return f'{self.get_full_name() or self.username} ({self.get_role_display()})'
