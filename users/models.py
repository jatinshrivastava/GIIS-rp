from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    Parent = 'Pa'
    Staff = 'St'
    
    
    Status_Choices = [
        (Parent, 'Parent'),
        (Staff, 'Staff'),
    ]
    student_name = models.CharField(max_length=60, blank=False, null=False, default='none')
    user_type = models.CharField(max_length=2,choices=Status_Choices,
        default=Parent)
    