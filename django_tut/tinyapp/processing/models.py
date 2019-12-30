from django.db import models

# Create your models here.
class urlstorage(models.Model):
    col = models.CharField(max_length=100)