from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=200)
    birthday = models.DateField()

    class Meta:
        abstract = True

class Actors(Person):
    pass
class Directors(Person):
    pass

class Movies(models.Model):
    title = models.CharField(max_length=300)
    plot = models.CharField(max_length=1000)
    actors = models.ManyToManyField(Actors)
    directors = models.ManyToManyField(Directors)

class Ratings(models.Model):
    stars = models.SmallIntegerField()

