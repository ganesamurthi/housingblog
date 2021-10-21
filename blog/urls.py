from django.urls import path
from .views import HomeView,ArticleDetailView,CategoryView,AboutView

# app_name = 'blog'
urlpatterns = [
    path('',HomeView.as_view(),name="home"),
    path('article/<str:slug>-<int:pk>',ArticleDetailView.as_view(),name="article_detail"),
    path('category/<str:cats>', CategoryView, name='category'),
    path('about_us/',AboutView, name='about_us'),
]
