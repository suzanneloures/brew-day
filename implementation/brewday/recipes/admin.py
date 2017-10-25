from django.contrib import admin
from .models import Recipe, Equipment, Ingredient

# Register your models here.
admin.site.register(Recipe)
admin.site.register(Equipment)
admin.site.register(Ingredient)
