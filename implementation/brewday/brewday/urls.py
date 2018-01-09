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

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/', views.access, name="login"),
    url(r'^register_user/', views.register_user, name="register_user"),
    url(r'^home/', views.home, name="home"),
    url(r'^index/', views.index),
    url(r'^recipes/', views.recipes, name="recipes"),
    url(r'^register-ingredient-additives/', views.register_ingredient1, name="ingredient1"),
    url(r'^register-ingredient-hops/', views.register_ingredient2, name="ingredient-hops"),
    url(r'^register-ingredient-malt/', views.register_ingredient3, name="ingredient3"),
    url(r'^register-ingredient-sugar/', views.register_ingredient4, name="ingredient4"),
    url(r'^register-ingredient-yeasts/', views.register_ingredient5, name="ingredient5"),
    url(r'^register-equipment-kettle/', views.register_equipment1, name="equipment1"),
    url(r'^register-equipment-fermenter/', views.register_equipment2, name="equipment2"),
    url(r'^register-equipment-filter/', views.register_equipment3, name="equipment3"),
    url(r'^register-equipment-grinder/', views.register_equipment4, name="equipment4"),
    url(r'^view_recipes/', views.view_recipes, name="view_recipes"),
    url(r'^register_equipment/', views.register_equipment1, name="register_equipment1"),
    url(r'^view_ingredients/', views.view_ingredients, name="view_ingredients"),

    
    









]
