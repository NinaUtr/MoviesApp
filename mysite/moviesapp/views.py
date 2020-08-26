from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin
from .models import Actors, Directors, Movies
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from rest_framework import viewsets
from . import serializers


class ActorList(ListView):
    model = Actors
    template_name = 'actors/list_actor.html'


class ActorDetailView(DetailView):
    model = Actors
    template_name = 'actors/detail_actor.html'


class ActorManage(PermissionRequiredMixin, ListView):
    model = Actors
    permission_required = 'moviesapp.change'
    template_name = 'actors/manage_actor.html'


class ActorCreate(PermissionRequiredMixin, CreateView):
    model = Actors
    permission_required = 'moviesapp.change'
    fields = '__all__'
    template_name = 'actors/new_actor.html'
    success_url = reverse_lazy('actors')


class ActorUpdate(PermissionRequiredMixin, UpdateView):
    model = Actors
    permission_required = 'moviesapp.change'
    fields = '__all__'
    template_name = 'actors/update_actor.html'
    success_url = reverse_lazy('manage_actor')

    def formatted_birthday(self):
        month = self.object.birthday.month
        day = self.object.birthday.day
        if self.object.birthday.month < 10:
            month = f"0{self.object.birthday.month}"
        if self.object.birthday.day < 10:
            day = f"0{self.object.birthday.day}"
        return f"{self.object.birthday.year}-{month}-{day}"


class ActorDelete(PermissionRequiredMixin, DeleteView):
    model = Actors
    permission_required = 'moviesapp.change'
    template_name = 'actors/delete_actor.html'
    success_url = reverse_lazy('manage_actor')


class ActorAPI(viewsets.ReadOnlyModelViewSet):
    queryset = Actors.objects.all()
    serializer_class = serializers.ActorSerializer


class DirectorList(ListView):
    model = Directors
    template_name = 'directors/list_director.html'


class DirectorDetailView(DetailView):
    model = Directors
    template_name = 'directors/detail_director.html'


class DirectorManage(PermissionRequiredMixin, ListView):
    model = Directors
    permission_required = 'moviesapp.change'
    template_name = 'directors/manage_director.html'


class DirectorCreate(PermissionRequiredMixin, CreateView):
    model = Directors
    fields = '__all__'
    permission_required = 'moviesapp.change'
    template_name = 'directors/new_director.html'
    success_url = reverse_lazy('directors')


class DirectorUpdate(PermissionRequiredMixin, UpdateView):
    model = Directors
    fields = '__all__'
    permission_required = 'moviesapp.change'
    template_name = 'directors/update_director.html'
    success_url = reverse_lazy('manage_director')

    def formatted_birthday(self):
        month = self.object.birthday.month
        day = self.object.birthday.day
        if self.object.birthday.month < 10:
            month = f"0{self.object.birthday.month}"
        if self.object.birthday.day < 10:
            day = f"0{self.object.birthday.day}"
        return f"{self.object.birthday.year}-{month}-{day}"


class DirectorDelete(PermissionRequiredMixin, DeleteView):
    model = Directors
    permission_required = 'moviesapp.change'
    template_name = 'directors/delete_director.html'
    success_url = reverse_lazy('manage_director')


class DirectorAPI(viewsets.ReadOnlyModelViewSet):
    queryset = Directors.objects.all()
    serializer_class = serializers.DirectorSerializer


class MovieList(ListView):
    model = Movies
    template_name = 'movies/list_movie.html'


class MovieDetailView(DetailView):
    model = Movies
    template_name = 'movies/detail_movie.html'


class MovieManage(PermissionRequiredMixin, ListView):
    model = Movies
    permission_required = 'moviesapp.change'
    template_name = 'movies/manage_movie.html'


class MovieCreate(PermissionRequiredMixin, CreateView):
    model = Movies
    permission_required = 'moviesapp.change'
    fields = '__all__'
    template_name = 'movies/new_movie.html'
    success_url = reverse_lazy('movies')

    def actors(self):
        return Actors.objects.all()

    def directors(self):
        return Directors.objects.all()


class MovieUpdate(PermissionRequiredMixin, UpdateView):
    model = Movies
    permission_required = 'moviesapp.change'
    fields = '__all__'
    template_name = 'movies/update_movie.html'
    success_url = reverse_lazy('manage_movie')

    def actors(self):
        return Actors.objects.all()

    def directors(self):
        return Directors.objects.all()

    def formatted_date(self):
        month = self.object.date.month
        day = self.object.date.day
        if self.object.date.month < 10:
            month = f"0{self.object.date.month}"
        if self.object.date.day < 10:
            day = f"0{self.object.date.day}"
        return f"{self.object.date.year}-{month}-{day}"


class MovieDelete(PermissionRequiredMixin, DeleteView):
    model = Movies
    permission_required = 'moviesapp.change'
    template_name = 'movies/delete_movie.html'
    success_url = reverse_lazy('manage_movie')


class MovieAPI(viewsets.ReadOnlyModelViewSet):
    queryset = Movies.objects.all()
    serializer_class = serializers.MovieSerializer
