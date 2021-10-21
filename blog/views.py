from django.shortcuts import render
from django.views.generic import ListView, DetailView
from blog.models import Post, Category
from blog.forms import PostForm
from django.urls import reverse_lazy


class HomeView(ListView):
    model = Post
    template_name = 'blog/home.html'
    ordering = ['-post_date']

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'blog/article_detail.html'

def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats.replace('-',' '))
    return render(request,'blog/categories.html',{'cats':cats.title().replace('-',' '), 'category_posts':category_posts})

def AboutView(request):
    return render(request,'blog/about.html',{})
