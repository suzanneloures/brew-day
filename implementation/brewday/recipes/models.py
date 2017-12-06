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
    type_ingredient = models.CharField(max_length=300)

class Equipment (models.Model):
    name = models.CharField(max_length=300)
    capacity = models.FloatField()
    unit_dimension = models.CharField(max_length=45)

class Production (models.Model):
    quantity_brew = models.FloatField()
    id_recipe = models.ForeignKey('Recipe', null=True)

class Recipe_Ingredient (models.Model):
    id_type_ingredient = models.ForeignKey('Type_Ingredient', null=True)
    id_recipe = models.ForeignKey('Recipe', null=True)
    id_ingredient = models.ForeignKey('Ingredient', null=True)
    quantity = models.FloatField()

class Recipe_Equipment (models.Model):
    id_recipe = models.ForeignKey('Recipe', null=True)
    id_ingredient = models.ForeignKey('Ingredient', null=True)
    quantity = models.FloatField()
    
class Type_Ingredient (models.Model):
    name = models.CharField(max_length=45)
