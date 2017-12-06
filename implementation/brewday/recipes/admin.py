from django.contrib import admin
from .models import Recipe, Equipment, Ingredient, Production, Recipe_Ingredient, Recipe_Equipment, Type_Ingredient

# Register your models here.
admin.site.register(Recipe)
admin.site.register(Equipment)
admin.site.register(Ingredient)
admin.site.register(Production)
admin.site.register(Recipe_Ingredient)
admin.site.register(Recipe_Equipment)
admin.site.register(Type_Ingredient)