from django.db import models

# Create your models here.
class Location(models.Model):
    location = models.CharField(max_length=100)
    user_id = models.IntegerField()