from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap

from blog.models import Post
from blog.sitemaps import Post_Sitemap, Static_Sitemap
from blog.views import ArticleDetailView, HomeView

sitemaps = {
    'posts':Post_Sitemap,
    'others': Static_Sitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('blog.urls')),
    path('members/', include('django.contrib.auth.urls')),
    path('members/',include('members.urls')),
    path('sitemap.xml',sitemap,{'sitemaps': sitemaps},name='django.contrib.sitemaps.views.sitemap'),
]
