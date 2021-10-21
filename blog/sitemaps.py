from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from blog.models import Post

class Static_Sitemap(Sitemap):

    priority = 1.0
    changefreq = "yearly"

    def items(self):
        return['about_us',]

    def location(self,item):
        return reverse(item)

class Post_Sitemap(Sitemap):
    changefreq = "daily"
    priority = 0.7

    def items(self):
        return Post.objects.all()

    # def location(self,item):
    #     return reverse(item)
