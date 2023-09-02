from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('OPS', 'Operation User'),
        ('CLIENT', 'Client User'),
    )
    user_type = models.CharField(choices=USER_TYPE_CHOICES, max_length=10)

class UploadedFile(models.Model):
    uploaded_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    file = models.FileField(upload_to='files/')