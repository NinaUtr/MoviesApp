from django.db import models
from datetime import datetime

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=200)
    birthday = models.DateField()

    def __str__(self):
        return self.name+' '+self.surname

    class Meta:
        abstract = True

class Actors(Person):
    pass
class Directors(Person):
    pass

class Movies(models.Model):
    title = models.CharField(max_length=300)
    plot = models.CharField(max_length=1000)
    date = models.DateField(default=datetime.now())
    actors = models.ManyToManyField(Actors)
    directors = models.ManyToManyField(Directors)

    def year_from_date(self):
        return self.date.strftime('%Y')

    def __str__(self):
        return self.title+' ('+str(self.year_from_date())+') '

class Ratings(models.Model):
    actor = models.OneToOneField(Actors, on_delete=models.CASCADE)
    stars = models.SmallIntegerField()

