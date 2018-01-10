"""brewday URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from recipes import views
from recipes.views import view_recipes

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/', views.access, name="login"),
    url(r'^register_user/', views.register_user, name="register_user"),
    url(r'^home/', views.home, name="home"),
    url(r'^index/',  views.index, name="index"),
    url(r'^recipes/', views.recipes, name="recipes"),
    url(r'^production/', views.production, name="production"),

    #Registros de URLS INGREDIENTES
    url(r'^register-ingredient-additives/', views.register_ingredient_additives, name="register_additives"),
    url(r'^register-ingredient-hops/', views.register_ingredient_hops, name="register_hops"),
    url(r'^register-ingredient-malt/', views.register_ingredient_malt, name="register_malt"),
    url(r'^register-ingredient-sugar/', views.register_ingredient_sugar, name="register_sugar"),
    url(r'^register-ingredient-yeasts/', views.register_ingredient_yeasts, name="register_yeasts"),
    #Registros de URLS EQUIPAMENTOS
    url(r'^register-equipment-fermenter/', views.register_equipment_fermenter, name="register_fermenter"),
    url(r'^register-equipment-filter/', views.register_equipment_filter, name="register_filter"),
    url(r'^register-equipment-grinder/', views.register_equipment_grinder, name="register_grinder"),
    url(r'^register-equipment-kettle/', views.register_equipment_kettle, name="register_kettle"),
    #Registros de URLS VIEWS
    url(r'^view_recipes/', view_recipes.as_view(), name="view_recipes"),
    url(r'^view_equipment/', views.view_equipment, name="view_equipment"),
    url(r'^view_ingredients/', views.view_ingredients, name="view_ingredients"),

    
    









]
