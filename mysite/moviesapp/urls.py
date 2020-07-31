from django.urls import path

from . import views

urlpatterns = [
    path('', views.helloWorld, name='helloWorld'),
    path('signup/', views.SignUp.as_view(), name='signup'),
]