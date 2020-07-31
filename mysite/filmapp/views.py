from django.http import HttpResponse
from django.shortcuts import render


def helloWorld(request):
    return render(request, 'filmapp/main_page.html')