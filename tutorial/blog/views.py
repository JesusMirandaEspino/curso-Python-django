from django.shortcuts import render, HttpResponse
from .models import Post



def home(request):
    posts = Post.objects.all()
    return render(request, "blog/home.html", {'posts': posts})
# Create your views here.


def post(request, id):
    post = Post.objects.get(id=id)
    return render(request, "blog/post.html", {'post': post})
