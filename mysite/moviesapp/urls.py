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
    path('actors/manage_actor', ListView.as_view(model=Actors, template_name='actors/manage_actor.html'),
         name='manage_actor'),
    path('actors/<pk>', DetailView.as_view(model=Actors, template_name='actors/detail_actor.html'),
         name='detail_actor'),
    path('actors/new/$',
         CreateView.as_view(model=Actors, template_name='actors/new_actor.html', success_url=reverse_lazy('actors'),
                            fields='__all__'), name='new_actor'),
    path('actors/<pk>/update',
         UpdateView.as_view(model=Actors, template_name='actors/update_actor.html', success_url=reverse_lazy('actors'),fields='__all__'),
         name='update_actor'),
    path('actors/<pk>/delete',
         DeleteView.as_view(model=Actors, template_name='actors/delete_actor.html', success_url=reverse_lazy('actors')),
         name='delete_actor'),

    path('directors/', views.DirectorList.as_view(), name='directors'),
    path('directors/manage_director', views.DirectorManage.as_view(), name='manage_director'),
    path('directors/<pk>', views.DirectorDetailView.as_view(), name='detail_director'),
    path('directors/new/$', views.DirectorCreate.as_view(), name='new_director'),
    path('directors/<pk>/update', views.DirectorUpdate.as_view(), name='update_director'),
    path('directors/<pk>/delete', views.DirectorDelete.as_view(), name='delete_director'),
    path('movies/', views.MovieList.as_view(), name='movies'),
    path('movies/manage_movie', views.MovieManage.as_view(), name='manage_movie'),
    path('movies/<pk>', views.MovieDetailView.as_view(), name='detail_movie'),
    path('movies/new/$', views.MovieCreate.as_view(), name='new_movie'),
    path('movies/<pk>/update', views.MovieUpdate.as_view(), name='update_movie'),
    path('movies/<pk>/delete', views.MovieDelete.as_view(), name='delete_movie')]
