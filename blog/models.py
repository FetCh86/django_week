from django.db import models
from django.utils import timezone
# Create your models here.
class Article(models.Model):
    titre = models.CharField(max_length=100)
    auteur = models.CharField(max_length=42)
    texte = models.TextField(null = True)
    date = models.DateTimeField(default=timezone.now,
                                verbose_name="Date de parution")
    categorie = models.ForeignKey('Categorie', on_delete=models.CASCADE)

    class Meta:
        verbose_name="article"
        ordering = ['date']

    def __str__(self):
        return self.titre

class Categorie(models.Model):
    nom = models.CharField(max_length=30)

    def __str__(self):
        return self.nom
