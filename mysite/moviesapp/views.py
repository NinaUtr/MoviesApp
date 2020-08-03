from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .models import Actors, Directors, Movies
from django.shortcuts import render


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

def all_actors(request):
    try:
        actors = Actors.object.all()
        return render(request, 'main_content/actors.html', {'actors': [actors]})
    except AttributeError:
        return render(request, 'main_content/actors.html', {'actors': []})

def all_directors(request):
    try:
        directors = Directors.object.all()
        return render(request, 'main_content/directors.html', {'directors': [directors]})
    except AttributeError:
        return render(request, 'main_content/directors.html', {'directors': []})

def all_movies(request):
    try:
        movies = Movies.object.all()
        return render(request, 'main_content/movies.html', {'movies': [movies]})
    except AttributeError:
        return render(request, 'main_content/movies.html', {'movies': []})