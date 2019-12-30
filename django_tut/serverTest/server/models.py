from django.db import models

# Create your models here.
class urlList(models.Model):
    url = models.CharField(max_length=100)

