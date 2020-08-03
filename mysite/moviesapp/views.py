from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .models import Actors, Directors, Movies
from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class ActorList(ListView):
    model = Actors
    template_name = 'actors/list_actor.html'

class ActorDetailView(DetailView):
    model = Actors
    template_name = 'actors/detail_actor.html'

class ActorCreate(CreateView):
    model = Actors
    fields = ['name', 'surname', 'description', 'birthday', 'photo']
    template_name = 'actors/new_actor.html'
    success_url = reverse_lazy('actors')

class ActorUpdate(UpdateView):
    model = Actors
    fields = ['name', 'surname', 'description', 'birthday', 'photo']
    template_name = 'actors/update_actor.html'
    success_url = reverse_lazy('actors')

class ActorDelete(DeleteView):
    model = Actors
    template_name = 'actors/delete_actor.html'
    success_url = reverse_lazy('actors')


class DirectorList(ListView):
    model = Directors
    template_name = 'directors/list_director.html'

class DirectorDetailView(DetailView):
    model = Directors
    template_name = 'directors/detail_director.html'

class DirectorCreate(CreateView):
    model = Directors
    fields = ['name', 'surname', 'description', 'birthday', 'photo']
    template_name = 'directors/new_director.html'
    success_url = reverse_lazy('directors')

class DirectorUpdate(UpdateView):
    model = Directors
    fields = ['name', 'surname', 'description', 'birthday', 'photo']
    template_name = 'directors/update_director.html'
    success_url = reverse_lazy('directors')

class DirectorDelete(DeleteView):
    model = Directors
    template_name = 'directors/delete_director.html'
    success_url = reverse_lazy('directors')



def all_movies(request):
    try:
        movies = Movies.objects.all()
        return render(request, 'main_content/list_movie.html', {'movies': movies})
    except AttributeError:
        return render(request, 'main_content/list_movie.html', {'movies': []})