from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *


class NewsHome(ListView):
    model = News
    template_name = 'blog/home_news_list.html'
    context_object_name = 'news'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

class NewsByCategory(ListView):
    model = News
    template_name = 'blog/home_news_list.html'
    context_object_name = 'news'

    def get_queryset(self):
        return News.objects.filter(cat_id=self.kwargs['cat_id'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

class ViewNews(DetailView):
    model = News
    context_object_name = 'news_item'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context