from django.urls import path

from . import views

urlpatterns = [
    path('accounts/signup/', views.SignUp.as_view(), name='signup'),
    path('actors/', views.ActorList.as_view(), name='actors'),
    path('actors/<pk>', views.ActorDetailView.as_view(), name='detail_actor'),
    path('actors/<pk>/new', views.ActorCreate.as_view(), name='new_actor'),
    path('actors/<pk>/update', views.ActorUpdate.as_view(), name='update_actor'),
    path('actors/<pk>/delete', views.ActorDelete.as_view(), name='delete_actor'),
    path('directors/', views.DirectorList.as_view(), name='directors'),
    path('directors/<pk>', views.DirectorDetailView.as_view(), name='detail_director'),
    path('directors/<pk>/new', views.DirectorCreate.as_view(), name='new_director'),
    path('directors/<pk>/update', views.DirectorUpdate.as_view(), name='update_director'),
    path('directors/<pk>/delete', views.DirectorDelete.as_view(), name='delete_director'),
    path('movies/', views.MovieList.as_view(), name='movies'),
    path('movies/<pk>', views.MovieDetailView.as_view(), name='detail_movie'),
    path('movies/<pk>/new', views.MovieCreate.as_view(), name='new_movie'),
    path('movies/<pk>/update', views.MovieUpdate.as_view(), name='update_movie'),
    path('movies/<pk>/delete', views.MovieDelete.as_view(), name='delete_movie')]