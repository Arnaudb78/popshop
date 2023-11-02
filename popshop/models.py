from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

# Create your models here.


User = get_user_model()


# class User(models.Model):
#     name = models.CharField(max_length=100)
#     mail = models.EmailField()
#     email = models.EmailField()
#     password = models.CharField(max_length=50)


class Categories(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Catégorie"
        verbose_name_plural = "Catégories"


class Articles(models.Model):
    class Status(models.TextChoices):
        DRAFT = "DF", "Brouillon"
        PUBLISHED = "PB", "Publié"
        CLOSED = "CL", "Fermé"

    # champs automatique
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # champs table
    status = models.CharField(
        max_length=2, choices=Status.choices, default=Status.DRAFT
    )
    title = models.CharField(max_length=255)
    content = models.TextField("Contenu", blank=True)
    published_at = models.DateTimeField(
        verbose_name="Date de publication", default=timezone.now, blank=True
    )

    category = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True)

    # image
    thumb = models.ImageField(upload_to="images/%Y/%m/", blank=True)
    cover = models.ImageField(upload_to="images/%Y/%m/", blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"
