from django.contrib import admin
from .models import Actors, Directors, Movies

admin.site.register(Actors)
admin.site.register(Directors)
admin.site.register(Movies)
