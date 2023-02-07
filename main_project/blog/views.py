from django.shortcuts import render
from django.views.generic import ListView
from .models import *


class NewsHome(ListView):
    model = News
    template_name = 'blog/home_news_list.html'
