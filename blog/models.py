from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField
from django.utils.text import slugify
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    snippet = models.CharField(max_length=255,default='Click above to read the article')
    body = RichTextField(blank=True,null=True)
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=255, default='uncategorised')
    slug = models.SlugField(default=' ', editable=False, max_length=200, null = False)

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):

        kwargs = {
            'pk':self.id,
            'slug':self.slug
        }
        return reverse('article_detail',kwargs=kwargs)

    def save(self, *args, **kwargs):
        value = self.title_tag
        self.slug= slugify(value,allow_unicode=True)
        super().save(*args,**kwargs)

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')
