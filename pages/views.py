from django.shortcuts import render,HttpResponse,redirect
from listings.models import *
from django.contrib.auth.models import User
from django.contrib import messages,auth
import random, re

def password_check(passwd):
      
    SpecialSym =['$', '@', '#', '%']
    val = True
    l=[]
    if len(passwd) < 6:
        l.append('Length of the password should be at least 6')
        val = False
        l.append(val)
        return l  
    elif len(passwd) > 12:
        l.append('Length of the password should be not be greater than 12')
        val = False
        l.append(val)
        return l  
    elif not any(char.isdigit() for char in passwd):
        l.append('Password should have at least one numeral')
        val = False
        l.append(val)
        return l  
    elif not any(char.isupper() for char in passwd):
        l.append('Password should have at least one uppercase letter')
        val = False
        l.append(val)
        return l 
    elif not any(char.islower() for char in passwd):
        l.append('Password should have at least one lowercase letter')
        val = False
        l.append(val)
        return l
    elif not any(char in SpecialSym for char in passwd):
        l.append('Password should have at least one of the symbols $@#')
        val = False
        l.append(val)
        return l

    if val:
        l.append("Password Valid")
        l.append(val)
        return l


def index(request):
    kitchen=Kitchen.objects.all().filter(is_hot=True).filter(is_published=True)
    clothing=Clothing.objects.all().filter(is_hot=True).filter(is_published=True)
    gym=Gym.objects.all().filter(is_hot=True).filter(is_published=True)
    shoes=Shoes.objects.all().filter(is_hot=True).filter(is_published=True)
    electronics=Electronics.objects.all().filter(is_hot=True).filter(is_published=True)
    everyday_thing=Daliy_Use.objects.all().filter(is_hot=True).filter(is_published=True)
    
    
    listings=Kitchen.objects.all().filter(is_published=True)
    context ={
        'listings':listings,
        'kitchen':kitchen,
        'clothing':clothing,
        'gym':gym,
        'shoes':shoes,
        'electronics':electronics,
        'everyday_thing':everyday_thing,
        
    }
    return render(request,'pages/index.html',context)


def clothing(request):
    products=Clothing.objects.all().filter(is_published=True)
    context ={
        'products':products,
    }
    return render(request,'pages/products/clothing.html',context)

def gym(request):
    products=Gym.objects.all().filter(is_published=True)
    context ={
        'products':products,
    }
    return render(request,'pages/products/gym.html',context)

def electronics(request):
    products=Electronics.objects.all().filter(is_published=True)
    context ={
        'products':products,
    }
    return render(request,'pages/products/electronics.html',context)

def shoes(request):
    products=Shoes.objects.all().filter(is_published=True)
    context ={
        'products':products,
    }
    return render(request,'pages/products/shoes.html',context)

def kitchen(request):
    products=Kitchen.objects.all().filter(is_published=True)
    context ={
        'products':products,
    }
    return render(request,'pages/products/kitchen.html',context)

def everyday_things(request):
    products=Daliy_Use.objects.all().filter(is_published=True)
    context ={
        'products':products,
    }
    return render(request,'pages/products/everyday_things.html',context)



def login(request):
    if request.method == 'POST':
        username=request.POST['uname']
        password=request.POST['password']

        user =auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request,user)
            messages.success(request,'You are now logged in')
            return redirect('index')
        else:
            messages.error(request,'Invalid Credintials')
            return redirect('login')
    else:        
        return render(request,'pages/login.html')

def register(request):
    if request.method== 'POST':
                # get form values
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        username = request.POST['uname']
        email=request.POST['email']
        password= request.POST['password']
        password2= request.POST['password2']

        # check if password match
        if password==password2:
            inf = password_check(password);
            if(inf[1]):
                if User.objects.filter(username=username).exists():
                    messages.error(request,'That username is used')
                    return redirect('register')
                else: 
                    if User.objects.filter(email=email).exists():
                        messages.error(request,'The email is already used.')
                        return redirect('register')
                    else:
                            # looks good
                            user=User.objects.create_user(username=username, password=password,email=email,first_name=first_name,last_name=last_name)
                            #Login after user
                            # auth.login(request,user)
                            # messages.success(request, "You are logged in")
                            # return redirect('index')

                            user.save();
                            messages.success(request, 'You are now registered and can log in')
                            return redirect('login')

            else:
                messages.error(request,inf[0])
                return redirect('register')

                        
            
        else:
            messages.error(request,'Passwords do not match')
            return redirect('register')
    else:
        return render(request,'pages/register.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request,'You are now logged out')
        return redirect('index')
