from django.urls import reverse_lazy
from .models import Actors, Directors, Movies, User
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


class Register(CreateView):
    model = User
    fields = ['email', 'password']
    success_url = reverse_lazy('home')
    template_name = 'registration/register.html'


class ActorList(ListView):
    model = Actors
    template_name = 'actors/list_actor.html'


class ActorDetailView(DetailView):
    model = Actors
    template_name = 'actors/detail_actor.html'


class ActorCreate(CreateView):
    model = Actors
    fields = '__all__'
    template_name = 'actors/new_actor.html'
    success_url = reverse_lazy('actors')


class ActorUpdate(UpdateView):
    model = Actors
    fields = '__all__'
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
    fields = '__all__'
    template_name = 'directors/new_director.html'
    success_url = reverse_lazy('directors')


class DirectorUpdate(UpdateView):
    model = Directors
    fields = '__all__'
    template_name = 'directors/update_director.html'
    success_url = reverse_lazy('directors')


class DirectorDelete(DeleteView):
    model = Directors
    template_name = 'directors/delete_director.html'
    success_url = reverse_lazy('directors')


class MovieList(ListView):
    model = Movies
    template_name = 'movies/list_movie.html'


class MovieDetailView(DetailView):
    model = Movies
    template_name = 'movies/detail_movie.html'


class MovieCreate(CreateView):
    model = Movies
    fields = '__all__'
    template_name = 'movies/new_movie.html'
    success_url = reverse_lazy('movies')


class MovieUpdate(UpdateView):
    model = Movies
    fields = '__all__'
    template_name = 'movies/update_movie.html'
    success_url = reverse_lazy('movies')


class MovieDelete(DeleteView):
    model = Movies
    template_name = 'movies/delete_movie.html'
    success_url = reverse_lazy('movies')
