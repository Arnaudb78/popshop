from django.shortcuts import render
from django.views.generic import ListView
from .models import Articles, Categories


# Create your views here.
def CategoryList(request, category_id):
    # aller chercher la categorie demandée
    currentCategory = Categories.objects.get(pk=category_id)
    # aller cherher les articles de la catégorie
    articles = Articles.objects.filter(category=currentCategory)
    # définir un "context" (les infos à afficher)
    context = {
        "title": currentCategory.title,
        "articles": articles,
    }


class ArticleList(ListView):
    model = Articles
    template_name = "article_list.html"
    context_object_name = "articles"
