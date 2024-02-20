from django.shortcuts import render
from .models import Post
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, DeleteView, ListView, UpdateView


# Shows a specific blog post.
class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_details.html'

# List all the blog posts.
class BlogListView(ListView):
    model = Post
    template_name = 'home.html'

class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'author', 'body']

class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')

class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']