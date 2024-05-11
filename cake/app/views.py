from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from .models import Cake,UserProfile
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse



# Create your views here.

def index(request):
    return render(request,'index.html')




def register(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        email=request.POST['email']

        if not User.objects.filter(username=username).exists():
            user=User.objects.create_user(username=username,email=email,password=password)
            UserProfile.objects.create(user)

            login(request,user)
            return redirect('index')

        else:
          pass

    return render(request,'register.html')            
        

def user_login(request):
    if request.method=='POST':
        username=request.POST['username']   
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('index')  

        else:
            messages.error(request,'Invalid username or password')
            return render(request,'login.html')

    return render(request,'login.html')
    
@login_required(login_url='login')
def app(request):
    
    return render(request,'order.html')

def ele(request):   

    if request.method=='POST':
       name=request.POST['name']
       email=request.POST['email']
       mobile=request.POST['mobilenumber']
       address=request.POST['address']
       quantity=request.POST['quantity']
       description=request.POST['description']

       context={
        
        'user':name,
        'email':email,
        'mobile':mobile,
        'address':address,
        'quantity':quantity,
        'description':description,
        
       }
       obj=Cake()
        
       obj.name=name
       obj.email=email
       obj.mobilenumber=mobile
       obj.address=address
       obj.quantity=quantity
       obj.description=description
        
       obj.save()
        
       return render(request,'order.html',context)    


def user_logout(request):
    logout(request)
    return redirect("index")                   

