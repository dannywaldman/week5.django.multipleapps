from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse('placeholder to later display all the list of users')

def login(request):
    return HttpResponse('placeholder for users to login')

def new(request):
    return HttpResponse('placeholder for users to create a new user record')            
