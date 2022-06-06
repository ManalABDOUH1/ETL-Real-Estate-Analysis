from django.db import models

# Create your models here.

class Location(models. Model):
    id = models.IntegerField(primary_key=True)
    Title  = models.CharField(max_length=300)
    Location  = models.CharField(max_length=300)
    Price  = models.CharField(max_length=300)
    Caracteristiques  = models.CharField(max_length=500)
    Pieces  = models.CharField(max_length=500)
    Description  = models.CharField(max_length=500)
    Pictures  = models.CharField(max_length=500)
    Telephone  = models.CharField(max_length=300)
    Duree  = models.CharField(max_length=300)
    Surface  = models.CharField(max_length=300)


class Vente(models. Model):
    id = models.IntegerField(primary_key=True)
    Title  = models.CharField(max_length=300)
    Location  = models.CharField(max_length=300)
    Price  = models.CharField(max_length=300)
    Caracteristiques  = models.CharField(max_length=500)
    Pieces  = models.CharField(max_length=500)
    Description  = models.CharField(max_length=500)
    Pictures  = models.CharField(max_length=500)
    Telephone  = models.CharField(max_length=300)
    Surface  = models.CharField(max_length=300)