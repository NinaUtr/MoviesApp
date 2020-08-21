from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=200)
    description = models.TextField(max_length=1000, null=True, blank=True)
    birthday = models.DateField(default="2000-01-01")
    photo = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f"{self.name} {self.surname}"

    def short_description(self):
        return f"{self.description[:100]}"

    class Meta:
        abstract = True


class Actors(Person):
    pass


class Directors(Person):
    pass


class Movies(models.Model):
    title = models.CharField(max_length=300, unique=True)
    plot = models.TextField(max_length=1000, null=True)
    date = models.DateField(default="2000-01-01")
    actors = models.ManyToManyField(Actors, blank=True)
    directors = models.ManyToManyField(Directors, blank=True)
    poster = models.URLField(max_length=200, null=True)

    def year_from_date(self):
        return self.date.strftime('%Y')

    def __str__(self):
        return f"{self.title} ({str(self.year_from_date())})"

    def get_actors(self):
        return self.actors.__str__()

    def short_plot(self):
        return f"{self.plot[:100]}"
