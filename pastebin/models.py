from django.db import models

# Create your models here.
class Post(models.Model):
    filename = models.CharField(max_length=64, primary_key=True)
    content = models.CharField(max_length=1024)
    timestamp = models.DateTimeField(auto_now=True)
