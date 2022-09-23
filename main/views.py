
from django.http import HttpResponse
from .models import Contact
from http.client import HTTPResponse
from django.shortcuts import render


def index(request):
    return render(request,"index.html",{'navbar':'index'})
def about(request):
    return render(request,"about.html",{'navbar': 'about'})
def contact(request):
    if request.method=="POST":
        newcontact=Contact()
        name=request.POST["name"]
        email=request.POST["email"]
        phone=request.POST["phone"]
        subject=request.POST["subject"]
        newcontact.name=name
        newcontact.email=email
        newcontact.phone=phone
        newcontact.subject=subject
        newcontact.save()

        return HttpResponse("<h1>THANKS FOR CONTACTING US</h1>")


    return render(request,"contact.html",{'navbar':'contact'})   
    
def pricing(request):
    return render(request,"pricing.html",{'navbar':'pricing'})    
def service(request):
    return render(request,"service.html",{'navbar':'service'})      
