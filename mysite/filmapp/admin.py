from django.contrib import admin
from .models import Actors, Directors, Movies

# Register your models here.
admin.site.register(Actors)
admin.site.register(Directors)
admin.site.register(Movies)