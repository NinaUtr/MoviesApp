from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import User

class Register(CreateView):
    model = User
    fields = ['email', 'password']
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'