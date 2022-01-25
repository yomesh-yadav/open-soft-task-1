from contextlib import redirect_stderr, redirect_stdout
from imaplib import _Authenticator
from os import name
from telnetlib import AUTHENTICATION
from tkinter import Entry
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import person_user

def home(request):
    return render(request,"autheri/index.html")
def signup(request):
    if request.method == "POST":
        name = request.POST['name']
        rollnum = request.POST['rollnumber']
        email = request.POST['email']
        passworry = request.POST['passworry']

        student_details= person_user(name=name,rollnumber=rollnum,email=email,password=passworry)
        student_details.save()

        messages.success(request,"accunt successfully created")
        return redirect('/signin')


    return render(request,"autheri/signup.html")
def signin(request):
    data={}
    if request.method=='POST':
            rollnumber = request.POST['rollnumber']
            passw=request.POST['passw']

            check = person_user.objects.get(rollnumber=rollnumber)
            if check==Entry.DoesNotExist:
                messages.error("user doesnot exists")
                return render(request,"autheri/signin.html")
            elif check.password==passw :
                temp = check.name
                data={name:temp}

                return render(request,"autheri/index.html",data=data)
            else:
                return render(request,"autheri/signin.html")
    return render(request,"autheri/signin.html")


def signout(request):
    logout(request)
    messages.success(request,"loged out successfully")
    return render(request,"autheri/index.html")
    