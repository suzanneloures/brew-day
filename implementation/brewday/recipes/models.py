from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.

class Recipe (models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=300)
    type_brew = models.CharField(max_length=300)
    description = models.TextField()
    ingredients = models.ManyToManyField('Ingredient', through='Recipe_Ingredient', through_fields=('recipe','ingredient') , null=True)
    def __str__(self):
        return self.title

class BrewDay():
    recipe_id = 0
    quantity = 0
    equip_id = 0

class Ingredient (models.Model):  # tipo de ingrediente criar 
    user = models.ForeignKey(User)
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
    YEAR_IN_SCHOOL_CHOICES = (
    ('L', 'Litre'),
    ('M3', 'Cubic Metric'),
    ('GAL', 'Gallon'))
    name = models.CharField(max_length=300)
    medida = models.CharField(max_length=3,choices=YEAR_IN_SCHOOL_CHOICES,default='L')
    capacity = models.FloatField()
    #unit_dimension = models.CharField(max_length=45)
    type_equipment = models.ForeignKey('Type_Equipment', null=True)
    description = models.TextField()
    user = models.ForeignKey(User)

    def __str__(self):
        return self.name

class Production (models.Model):
    date = models.DateField(null=True, default=datetime.date.today)
    user = models.ForeignKey(User)
    quantity_brew = models.FloatField()
    id_recipe = models.ForeignKey('Recipe', null=True)

class Recipe_Ingredient (models.Model):
    #id_type_ingredient = models.ForeignKey('Type_Ingredient', null=True)
    recipe = models.ForeignKey('Recipe', null=True)
    ingredient = models.ForeignKey('Ingredient', null=True)
    quantity = models.FloatField()

class Recipe_Equipment (models.Model):
    id_recipe = models.ForeignKey('Recipe', null=True)
    id_ingredient = models.ForeignKey('Ingredient', null=True)
    quantity = models.FloatField()
    
class Type_Ingredient (models.Model):
    name = models.CharField(max_length=45)
    
    def __str__(self):
        return self.name

class Type_Equipment (models.Model):
    name = models.CharField(max_length=45)

    def __str__(self):
        return self.name
class Stock (models.Model):
    user = models.ForeignKey(User, unique=True)

class User_Ingredient (models.Model):
    user = models.ForeignKey(User, unique=True)
    quantity = models.FloatField()