from django.urls import path

from . import views

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('actors/', views.all_actors, name='actors'),
    path('directors/', views.all_directors, name='directors'),
    path('movies/', views.all_movies, name='movies')]