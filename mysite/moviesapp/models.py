from django.utils.timezone import now
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    """User model."""

    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()


class Person(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=200)
    description = models.TextField(max_length=1000, null=True)
    birthday = models.DateField(default=now())
    photo = models.URLField(max_length=200, null=True)

    def __str__(self):
        return f"{self.name} {self.surname}"

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
    poster = models.URLField(max_length=200, null=True)

    def year_from_date(self):
        return self.date.strftime('%Y')

    def __str__(self):
        return f"{self.title} ({str(self.year_from_date())})"


class StarRatings(models.Model):
    stars_choices = [(i, i) for i in range(0, 6)]
    stars = models.SmallIntegerField(choices=stars_choices)

    class Meta:
        abstract = True


class RatingsActors(StarRatings):
    actor = models.ForeignKey(Actors, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.actor.name} {self.actor.surname} ({str(self.stars)})"


class RatingsDirectors(StarRatings):
    director = models.ForeignKey(Directors, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.director.name} {self.director.surname} ({str(self.stars)})"


class RatingsMovies(StarRatings):
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.movie.title} ({str(self.stars)})"
