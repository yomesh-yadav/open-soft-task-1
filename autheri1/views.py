from contextlib import redirect_stderr, redirect_stdout
from imaplib import _Authenticator
from telnetlib import AUTHENTICATION
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import room
from django.http import JsonResponse
def home(request):
    

    # for i in range(50):
    #     r = room.objects.create(room_number=i)
    #     r.save()
    
    
    return render(request,"autheri/index.html")
def signup(request):
    if request.method == "POST":
        name = request.POST['name']
        rollnum = request.POST['rollnumber']
        
        email = request.POST['email']
        passw = request.POST['passworry']

        myuser=User.objects.create_user( username=rollnum,email=email, password=passw)
       
        myuser.first_name=name
        myuser.save()
        messages.success(request,"accunt successfully created")
        return redirect('/signin')


    return render(request,"autheri/signup.html")
def signin(request):
    data={}
    inte= room.objects.all()
   
    if request.method=='POST':
            rollnum = request.POST['rollnumber']
            passw=request.POST['passw']
            User=authenticate(username=rollnum, password=passw)
            print(User.username)
            if  User is not None:
                login(request,User)
                data={'name':User.first_name,
                'hell':inte,
                }
                return render(request,"autheri/index.html",data)
            else:
                messages.error(request,"bad credentials")
                return render(request,"autheri/signin.html",data)
    return render(request,"autheri/signin.html")


def signout(request):
    logout(request)
    messages.success(request,"loged out successfully")
    return render(request,"autheri/index.html")

def room_data(request):
    if request.method=="POST":
        print(request.user)
        uuser = request.user
        inte= room.objects.all()
        print(request.POST.get('person_name'))
        name = request.POST['person_name']
        rnum= request.POST['rno']
        room_info = room.objects.get(room_number=rnum)
        room_info.person_name=name
        room_info.status=True
        room_info.save()
        data={
                    'name':uuser.first_name,
                    'hell':inte,
            }
        messages.success(request,"room was alloted successfully")
        return render(request,"autheri/index.html",data)
    return HttpResponse("hello world")
    