from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class OpsCliUsers(AbstractUser):
    USER_TYPE_CHOICES = (
        ('OPS', 'Operation User'),
        ('CLIENT', 'Client User'),
    )
    user_type = models.CharField(choices=USER_TYPE_CHOICES, max_length=10)
    username = models.CharField(max_length=40)
    email = models.EmailField()

class UploadFile(models.Model):
    uploaded_by = models.ForeignKey(OpsCliUsers, on_delete=models.CASCADE)
    file = models.FileField(upload_to='files/')