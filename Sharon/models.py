# Create your models here.
# sharon/models.py

# Sharon/models.py
from django.db import models

class UserInformation(models.Model):
    name = models.CharField(max_length=255)
    education = models.CharField(max_length=255)
    job = models.CharField(max_length=255)
    programming = models.TextField()
