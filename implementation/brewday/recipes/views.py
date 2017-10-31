from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse 

def login(request):
	return render(request, "login.html")
	

def register(request):
    return render(request,"register.html")

