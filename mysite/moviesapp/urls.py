from django.urls import path

from . import views

urlpatterns = [
    path('signup/', views.SignUp.as_view()),
    path('actors/', views.ActorList.as_view(), name='actors'),
    path('actors/<pk>', views.ActorDetailView.as_view(), name= 'detail_actor'),
    path('actors/new', views.ActorCreate.as_view(), name='new_actor'),
    path('actors/<pk>/update', views.ActorUpdate.as_view(), name='update_actor'),
    path('actors/<pk>/delete', views.ActorDelete.as_view(), name='delete_actor'),
    path('directors/', views.DirectorList.as_view(), name='directors'),
    path('directors/<pk>', views.DirectorDetailView.as_view(), name='detail_director'),
    path('directors/new', views.DirectorCreate.as_view(), name='new_director'),
    path('directors/<pk>/update', views.DirectorUpdate.as_view(), name='update_director'),
    path('directors/<pk>/delete', views.DirectorDelete.as_view(), name='delete_director'),
    path('movies/', views.all_movies, name='movies')]