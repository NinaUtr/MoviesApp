from django.db import models

# Create your models here.
class Actors(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=200)
    birthday = models.DateTimeField()

