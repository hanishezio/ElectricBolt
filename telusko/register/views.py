from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from .models import Registration
from .forms import NewRegister
 
# Create your views here.
def registration(request):
    if request.method == 'POST':
        print("a")
          
        print(request.POST.get('first_name')) 
        a=Registration(first_name=request.POST.get('first_name'),last_name= request.POST.get('last_name'),username= request.POST.get('username'),location= request.POST.get('location'),email= request.POST.get('email'),phone= request.POST.get('phone')) 
        a.save()    
        # if request.POST.get('first_name') and request.POST.get('last_name') and request.POST.get('username') and  request.POST.get('location') and request.POST.get('email') and request.POST.get('phone'): 
        #     post=Registration()
        #     post.first_name= request.POST.get('first_name')
        #     post.last_name= request.POST.get('last_name')
        #     post.username= request.POST.get('username')
        #     post.location= request.POST.get('location')
        #     post.email= request.POST.get('email')
        #     #post.phone= request.POST.get('phone')             
        #     post.save()
            
        print("User Created")
        return redirect('location')       
        
        
            
    else:
        return render(request,'register.html')

        
    



# form = NewRegister(request.POST)
        # if form.is_valid():
        #     # process form data
        #     obj = Registration() #gets new object
        #     obj.first_name = form.cleaned_data['first_name']
        #     obj.last_name = form.cleaned_data['last_name']
        #     obj.username = form.cleaned_data['username']
        #     obj.location = form.cleaned_data['location']
        #     obj.email = form.cleaned_data['email']
        #     obj.phone = form.cleaned_data['phone']
        #     #finally save the object in db
        #     obj.save()
        #     print("User Created")
        #     return HttpResponseRedirect('home.html')