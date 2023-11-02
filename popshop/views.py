from django.shortcuts import render
from django.views.generic import ListView
from .models import Articles, Categories

# Create your views here.


class ArticleList(ListView):
    model = Articles
    template_name = "article_list.html"
    context_object_name = "articles"
