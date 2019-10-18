from django.shortcuts import render
from .models import Post
from  django.views.generic import ListView, DetailView
# Create your views here.


class HomeView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post.html'
    context_object_name = 'post'
