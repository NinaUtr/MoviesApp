from django.contrib import admin
from .models import Actors, Directors, Movies,Ratings

# Register your models here.
admin.site.register(Actors)
admin.site.register(Directors)
admin.site.register(Movies)
admin.site.register(Ratings)