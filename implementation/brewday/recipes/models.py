from django.db import models

# Create your models here.

class Recipe (models.Model):
    title = models.CharField(max_length=300)
    type_brew = models.CharField(max_length=300)
    description = models.TextField()
    id_equipment = models.ForeignKey('Equipment', null=True)

class Ingredient (models.Model):  # tipo de ingrediente criar 
    name = models.CharField(max_length=300)
    unity = models.FloatField() #Medida absoluta será medido em miligramas
    quantity = models.FloatField()

class Equipment (models.Model):
    name = models.CharField(max_length=300)
    capacity = models.FloatField()
    unit_dimension = models.TextField()

class Production (models.Model):
    quantity_brew = models.FloatField()
    

    

   
