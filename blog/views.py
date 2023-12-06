from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView


# Create your views here.

class BlogPage(ListView):
    template_name  = 'index.html'
    queryset  = Post.objects.filter(status = 'published')
    context_object_name = 'posts'


class BlogDetails(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'details.html'


