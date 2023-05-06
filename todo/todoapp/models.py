from django.db import models

# Create your models here.
class User(models.Model):
    task_name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now=True)
    