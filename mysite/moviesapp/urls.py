from django.urls import path
from .models import Actors, Directors, Movies, User
from . import views
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy

urlpatterns = [
    path('register/', views.Register.as_view(), name='register'),
    path('actors/', ListView.as_view(model=Actors, template_name='actors/list_actor.html'), name='actors'),
    path('actors/manage_actor', ListView.as_view(model=Actors, template_name='actors/manage_actor.html'),name='manage_actor'),
    path('actors/<pk>', DetailView.as_view(model=Actors, template_name='actors/detail_actor.html'), name='detail_actor'),
    path('actors/new/$',CreateView.as_view(model=Actors, template_name='actors/new_actor.html', success_url=reverse_lazy('actors'),fields='__all__'), name='new_actor'),
    path('actors/<pk>/update',UpdateView.as_view(model=Actors, template_name='actors/update_actor.html', success_url=reverse_lazy('actors'),fields='__all__'),name='update_actor'),
    path('actors/<pk>/delete',DeleteView.as_view(model=Actors, template_name='actors/delete_actor.html', success_url=reverse_lazy('actors')),name='delete_actor'),
    path('directors/', ListView.as_view(model=Directors, template_name='directors/list_director.html'), name='directors'),
    path('directors/manage_director', ListView.as_view(model=Directors, template_name='directors/manage_director.html'),name='manage_director'),
    path('directors/<pk>', DetailView.as_view(model=Directors, template_name='directors/detail_director.html'),name='detail_director'),
    path('directors/new/$',CreateView.as_view(model=Directors, template_name='directors/new_director.html', success_url=reverse_lazy('directors'),fields='__all__'), name='new_director'),
    path('directors/<pk>/update',UpdateView.as_view(model=Directors, template_name='directors/update_director.html', success_url=reverse_lazy('directors'),fields='__all__'), name='update_director'),
    path('directors/<pk>/delete',DeleteView.as_view(model=Directors, template_name='directors/delete_director.html', success_url=reverse_lazy('directors')),name='delete_director'),
    path('movies/', ListView.as_view(model=Movies, template_name='movies/list_movie.html'), name='movies'),
    path('movies/manage_movie', ListView.as_view(model=Movies, template_name='movies/manage_movie.html'),name='manage_movie'),
    path('movies/<pk>', DetailView.as_view(model=Movies, template_name='movies/detail_movie.html'),name='detail_movie'),
    path('movies/new/$',CreateView.as_view(model=Movies, template_name='movies/new_movie.html', success_url=reverse_lazy('movies'),fields='__all__'), name='new_movie'),
    path('movies/<pk>/update',UpdateView.as_view(model=Movies, template_name='movies/update_movie.html', success_url=reverse_lazy('movies'),fields='__all__'), name='update_movie'),
    path('movies/<pk>/delete',DeleteView.as_view(model=Movies, template_name='movies/delete_movie.html', success_url=reverse_lazy('movies')),name='delete_movie')]
