from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse 
from django.contrib.auth.models import User

def access(request):
    if request.method == 'POST':
        id_user = request.POST['user'] #pega o valor inserido no campo email
        password =  request.POST['pass']
        auth_user = authenticate(request, username = id_user, password = password)
        if auth_user is None:
            return render(request, "register.html")
        else:
            login(request,auth_user)
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
        user = User.objects.create_user(email,email,password)
        user.first_name = name
        user.last_name = lname
        user.save() 
        return render(request, "confirm.html" )

def confirm(request):
	return render(request, "confirm.html")

def home(request):
	return render(request, "home.html")
