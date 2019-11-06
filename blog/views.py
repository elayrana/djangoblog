from .models import Post
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.views.generic.edit import CreateView
from django.http import HttpRequest
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
#  Create your views here.


class HomeView(LoginRequiredMixin,ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post.html'
    context_object_name = 'post'


class PostCreateView(CreateView):
    model = Post
    template_name = 'blog/new_post.html'
    fields =['title', 'author', 'body']


class PostUpdateView(UpdateView):
    model = Post
    template_name = "blog/update_post.html"
    fields = ['title','author','body']


class PostDeleteView(DeleteView):
    model = Post
    template_name =  "blog/delete_post.html"
    success_url = reverse_lazy('blog:home')
