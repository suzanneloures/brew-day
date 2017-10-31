from django.db import models

# Create your models here.

class Recipe (models.Model):
    title = models.CharField(max_length=300)
    type_brew = models.CharField(max_length=300)
    description = models.TextField()

class Ingredient (models.Model):  # tipo de ingrediente criar 
    name = models.CharField(max_length=300)
    unity = models.FloatField() #Medida absoluta será medido em miligramas
    quantity = models.FloatField()

class Equipment (models.Model):
    name = models.CharField(max_length=300)
    capacity = models.FloatField()

   
