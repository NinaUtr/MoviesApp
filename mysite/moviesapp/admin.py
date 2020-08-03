from django.contrib import admin
from .models import Actors, Directors, Movies, RatingsMovies, RatingsActors, RatingsDirectors

# Register your models here.
admin.site.register(Actors)
admin.site.register(Directors)
admin.site.register(Movies)
admin.site.register(RatingsActors)
admin.site.register(RatingsDirectors)
admin.site.register(RatingsMovies)
