from django.db import models
from django.utils.timezone import now

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=200)
    description = models.TextField(max_length=1000, null=True)
    birthday = models.DateField(default=now())
    photo = models.ImageField(upload_to='photo', blank=True, null=True)

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
    plot = models.TextField(max_length=1000, null=True)
    date = models.DateField(default=now())
    actors = models.ManyToManyField(Actors)
    directors = models.ManyToManyField(Directors)
    poster = models.ImageField(upload_to='poster', blank=True, null=True)

    def year_from_date(self):
        return self.date.strftime('%Y')

    def __str__(self):
        return self.title+' ('+str(self.year_from_date())+') '

class StarRatings(models.Model):
    stars_choices = [(i,i) for i in range(0,6)]
    stars = models.SmallIntegerField(choices=stars_choices)

    class Meta:
        abstract = True

class RatingsActors(StarRatings):
    actor = models.ForeignKey(Actors, on_delete=models.CASCADE)

    def __str__(self):
        return self.actor.name+' '+self.actor.surname+' ('+str(self.stars)+') '

class RatingsDirectors(StarRatings):
    director = models.ForeignKey(Directors, on_delete=models.CASCADE)

    def __str__(self):
        return self.director.name+' '+self.director.surname+' ('+str(self.stars)+') '

class RatingsMovies(StarRatings):
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE)

    def __str__(self):
        return self.movie.title+' ('+str(self.stars)+') '
