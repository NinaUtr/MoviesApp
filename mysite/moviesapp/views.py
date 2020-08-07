from django.urls import reverse_lazy
from .models import User
from django.views.generic.edit import CreateView

class Register(CreateView):
    model = User
    fields = ['email', 'password']
    success_url = reverse_lazy('home')
    template_name = 'registration/register.html'
