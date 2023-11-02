from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.


User = get_user_model()


class User(models.Model):
    name = models.CharField(max_length=100)
    mail = models.EmailField()
    email = models.EmailField()
    password = models.CharField(max_length=50)


class Categories(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Catégorie"
        verbose_name_plural = "Catégories"


class Articles(models.Model):
    class Status(models.Model):
        DRAFT = "DF", "Brouillon"
        ONLINE = "OL", "En Ligne"
        CLOSED = "CL", "Fermé"

    # champs table
    status = models.Charfield(
        max_length=2, choices=Status.choices, default=Status.DRAFT
    )
    title = models.CharField(max_length=255)
    content = models.TextField("Contenu", blank=True)

    # cat
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True)

    # image
    thumb = models.ImageField(upload_to="images/%Y/%m/", blank=True)
    cover = models.ImageField(upload_to="images/%Y/%m/", blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"
