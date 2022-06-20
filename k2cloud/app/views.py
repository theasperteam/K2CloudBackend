from xmlrpc.client import ResponseError
from django.shortcuts import render
from .models import *
from django.http.response import JsonResponse
# Create your views here.

# Home Page 
def HomePage(request):
    return render(request, 'index.html')

# About Page
def AboutPage(request):
    return render(request, 'about.html')

# Team Page
def TeamPage(request):
    return render(request,'team.html')

# Contact Page
def ContactPage(request):
    if request.POST:
        x = request.POST
        name = x['name']
        email = x['email']
        contact = x['contact']
        message = x['message']
        
        try:
            data = Contact.objects.create(Name = name, Contact = contact, Email = email, Message = message )
            return render(request, 'contact.html', {"alert":1})
        except: 
            return render(request, 'contact.html', {"alert":0})
            
    else:
        return render(request,'contact.html')

# Services Page
def ServicePage(request):
    return render(request, 'services.html')