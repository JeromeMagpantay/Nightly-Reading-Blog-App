from django.shortcuts import render
from .models import Post
from django.views.generic import DetailView, ListView


# Shows a specific blog post.
class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_details.html'

# List all the blog posts.
class BlogListView(ListView):
    model = Post
    template_name = 'home.html'



