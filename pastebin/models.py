from django.db import models

# Create your models here.
class Post(models.Model):
    id = models.CharField(max_length=64, primary_key=True)
    filename = models.CharField(max_length=32)
    content = models.CharField(max_length=1024)
    timestamp = models.DateTimeField(auto_now=True)
