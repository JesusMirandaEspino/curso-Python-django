from django.shortcuts import render, HttpResponse


def home(request):
    return HttpResponse("<h1>Bienvenidos a mi blog</h1>")
# Create your views here.
