from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse 
from django.contrib.auth.models import User
from django.core.validators import validate_email
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from .models import Ingredient, Type_Ingredient
from django.shortcuts import get_object_or_404

def access(request):
    if request.method == 'POST':
        id_user = request.POST['user'] #pega o valor inserido no campo email
        password =  request.POST['pass']
        auth_user = authenticate(request, username = id_user, password = password)
        if auth_user is None:
            return render(request, "login.html", {"erro": True})
        else:
            login(request,auth_user)
            if request.user.is_superuser:
                return HttpResponseRedirect(reverse('admin:index'))
            else:
                return render(request, "home.html")
    else:
        return render (request, "login.html")

def register(request):
    if request.method  == 'GET':
        return render(request, "register.html")
    else:
        name = request.POST['name']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['pass']
        erros = []
        try:
            validate_email(email)
        except:
            erros.append('Email is invalid')
        if(len(name) == 0):
            erros.append("Name can't be blank")
        if(len(lname) == 0):
            erros.append("Last Name can't be blank")
        if(len(password) == 0):
            erros.append("Password can't be blank")

        if(len(erros)==0):
            user = User.objects.create_user(email,email,password)
            user.first_name = name
            user.last_name = lname
            user.save()       
            return HttpResponseRedirect(reverse('login'))
        else:
            return render(request, "register.html",{'erros': erros})

def confirm(request):
	return render(request, "confirm.html")

def home(request):
	return render(request, "home.html")

def index(request):
	return render(request, "index.html")

def recipes(request):
    malts = Ingredient.objects.filter(type_ingredient_id = 3)
    hops = Ingredient.objects.filter(type_ingredient_id = 1)
    yeasts = Ingredient.objects.filter(type_ingredient_id = 4)
    sugars = Ingredient.objects.filter(type_ingredient_id = 2)
    additives = Ingredient.objects.filter(type_ingredient_id = 5)
    conteudo = {'malts':malts, 'hops': hops, 'yeasts':yeasts, 'sugars': sugars, 'additives': additives}
    if request.method  == 'GET':
	    return render(request, "recipes2.html", conteudo)
    else:
        return render(request, "recipes2.html",conteudo)


def register_ingredients(request):
	return render(request, "register_ingredients.html")

def register_ingredient1(request):
    if request.method == 'GET':
        return render(request, "register_ingredient2_additives.html")
    else:
        additivesname = request.POST['additivesname']
        additivesquantity = request.POST['additivesquantity']
        unity = request.POST.get('additivesgrams',False)
        ingrediente = Ingredient()
        ingrediente.name = additivesname
        ingrediente.quantity = additivesquantity
        if unity:
            ingrediente.unity = 'GR'
        else:
            ingrediente.unity = 'KG'
        ingrediente.type_ingredient = get_object_or_404(Type_Ingredient, pk=5)

        ingrediente.save()
        conteudo = {'msg': 'Cadastrado com sucesso'}
        return render(request, "register_ingredient2_additives.html", conteudo)

def register_ingredient2(request):
    if request.method  == 'GET':
        return render(request, "register_ingredient2_hops.html")
    else:
        maltname = request.POST['maltname']
        hopsquantity = request.POST['hopsquantity']
        unity = request.POST.get('hopsgrams',False)
        #maltdescription = request.POST['maltdescription']
        ingrediente = Ingredient()
        ingrediente.name = maltname
        #ingrediente.unity = 0
        ingrediente.quantity = hopsquantity
        if unity:
            ingrediente.unity = 'GR'
        else:
            ingrediente.unity = 'KG'
        ingrediente.type_ingredient = get_object_or_404(Type_Ingredient, pk=1)

        ingrediente.save()

        conteudo = {'msg': 'Cadastrado com sucesso'}
        return render(request, "register_ingredient2_hops.html", conteudo)

def register_ingredient3(request):
    if request.method  == 'GET':
        return render(request, "register_ingredient2_malt.html")
    else:
        maltname = request.POST['maltname']
        maltquantity = request.POST['maltquantity']
        unity = request.POST.get('maltgrams',False)
        ingrediente = Ingredient()
        ingrediente.name = maltname
        #ingrediente.unity = 0
        ingrediente.quantity = maltquantity
        if unity:
            ingrediente.unity = 'GR'
        else:
            ingrediente.unity = 'KG'
        ingrediente.type_ingredient = get_object_or_404(Type_Ingredient, pk=3)

        ingrediente.save()

        conteudo = {'msg': 'Cadastrado com sucesso'}
        return render(request, "register_ingredient2_malt.html", conteudo)

def register_ingredient4(request):
    if request.method  == 'GET':
        return render(request, "register_ingredient2_sugar.html")
    else:
        sugarname = request.POST['sugarname']
        sugarquantity = request.POST['sugarquantity']
        unity = request.POST.get('imeasuregramssugar',False)
        ingrediente = Ingredient()
        ingrediente.name = sugarname
        #ingrediente.unity = 0
        ingrediente.quantity = sugarquantity
        if unity:
            ingrediente.unity = 'GR'
        else:
            ingrediente.unity = 'KG'
        ingrediente.type_ingredient = get_object_or_404(Type_Ingredient, pk=2)

        ingrediente.save()

        conteudo = {'msg': 'Cadastrado com sucesso'}
        return render(request, "register_ingredient2_sugar.html", conteudo)

def register_ingredient5(request):
    if request.method  == 'GET':
        return render(request, "register_ingredient2_yeasts.html")
    else:
        yeastsname = request.POST['yeastsname']
        yeastsquantity = request.POST['yeastsquantity']
        unity = request.POST.get('yeastsgrams',False)
        ingrediente = Ingredient()
        ingrediente.name = yeastsname
        #ingrediente.unity = 0
        ingrediente.quantity = yeastsquantity
        if unity:
            ingrediente.unity = 'GR'
        else:
            ingrediente.unity = 'KG'
        ingrediente.type_ingredient = get_object_or_404(Type_Ingredient, pk=4)

        ingrediente.save()

        conteudo = {'msg': 'Cadastrado com sucesso'}
        return render(request, "register_ingredient2_yeasts.html", conteudo)


def register_equipment1(request):
	return render(request, "register_equipment2_kettle.html")

def register_equipment2(request):
	return render(request, "register_equipment2_fermenter.html")

def register_equipment3(request):
	return render(request, "register_equipment2_filter.html")

def register_equipment4(request):
	return render(request, "register_equipment2_grinder.html")

def register_recipes1(request):
	return render(request, "register_recipes1.html")

def register_equipment1(request):
	return render(request, "register_equipment1.html")

