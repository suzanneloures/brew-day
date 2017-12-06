from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse 
from django.contrib.auth.models import User
from django.core.validators import validate_email
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import messages


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
	return render(request, "recipes2.html")

def register_ingredient1(request):
	return render(request, "register_ingredient2_additives.html")

def register_ingredient2(request):
	return render(request, "register_ingredient2_hops.html")

def register_ingredient3(request):
	return render(request, "register_ingredient2_malt.html")

def register_ingredient4(request):
	return render(request, "register_ingredient2_sugar.html")

def register_ingredient5(request):
	return render(request, "register_ingredient2_yeasts.html")

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

