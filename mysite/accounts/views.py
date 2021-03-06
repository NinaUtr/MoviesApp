from django.urls import reverse_lazy
from django.views import generic
from .forms import RegisterForm


class RegisterView(generic.CreateView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
