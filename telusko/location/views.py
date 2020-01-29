from django.contrib import messages
from django.shortcuts import render,redirect
from .models import Location 

# Create your views here.
def location(request):          
    return render(request,'location.html')
    
def homepage(request):          
    return redirect('home')
    
       