from django.db import models

# Create your models here.

class Recipe (models.Model):
    title = models.CharField(max_length=300)
    type_brew = models.CharField(max_length=300)
    description = models.TextField()

    def __str__(self):
        return self.title
    
class Ingredient (models.Model):  # tipo de ingrediente criar 
    YEAR_IN_SCHOOL_CHOICES = (
    ('GR', 'Gr'),
    ('KG', 'Kg'))
    name = models.CharField(max_length=300)
    unity = models.CharField(max_length=2,choices=YEAR_IN_SCHOOL_CHOICES,default='GR')
    quantity = models.FloatField()
    type_ingredient = models.ForeignKey('Type_Ingredient', null=True)

    def __str__(self):
        return self.name 

class Equipment (models.Model):
    name = models.CharField(max_length=300)
    capacity = models.FloatField()
    unit_dimension = models.CharField(max_length=45)

    def __str__(self):
        return self.name

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

    def __str__(self):
        return self.name
