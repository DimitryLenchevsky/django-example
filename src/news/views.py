from django.shortcuts import render
from django.views.generic import ListView, CreateView
from . import models


class CreateNews(CreateView):
    model = models.Articles
    template_name = 'news/create-news.html'
    fields = ('title', 'body')
    success_url = 'news/posts.html'