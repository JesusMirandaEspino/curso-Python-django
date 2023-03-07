from django.shortcuts import render, HttpResponse
from .models import Post



def home(request):
    posts = Post.objects.all()
    return render(request, "blog/home.html", {'posts': posts})
# Create your views here.
