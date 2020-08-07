from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.Register.as_view(), name='register'),
    path('actors/', views.ActorList.as_view(), name='actors'),
    path('actors/manage_actor', views.ActorManage.as_view(), name='manage_actor'),
    path('actors/<pk>', views.ActorDetailView.as_view(), name='detail_actor'),
    path('actors/new/$', views.ActorCreate.as_view(), name='new_actor'),
    path('actors/<pk>/update', views.ActorUpdate.as_view(), name='update_actor'),
    path('actors/<pk>/delete', views.ActorDelete.as_view(), name='delete_actor'),
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
