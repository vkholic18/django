from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.contrib.auth.models import User
from .models import Tasks
from django.urls import reverse_lazy
from todolist.forms import TaskForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
import random
import smtplib
import json

# Create your views here.
def todolist_home(request):
    return render(request,"todo/todo_home.html")
def userlogin(request):
    if request.method=='POST':
        username=request.POST["username"]
        password=request.POST["password"]
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("tasks")
        else:
            return HttpResponse("invalid Credentials")


    #if request.method=='POST':

    return render(request,"registration/login.html")
def register(request):
    context={"data":False}
    fixed_digits = 6
    OTP=random.randrange(111111, 999999, fixed_digits)
    server=smtplib.SMTP('smtp.gmail.com',587)

    server.starttls()
    server.login('saitejatest0592@gmail.com', 'aerizzwjrrjeegpe')
    msg= "Thanks for registering ToDo List Application "+ str(OTP) +" is your OTP"
    sender='saitejatest0592@gmail.com'

    if request.method=='POST':
        username=request.POST["username"]
        password=request.POST["password"]
        password1=request.POST["password1"]
        server.sendmail(sender,username,msg)
        print("mail sent")


        if password==password1:
            u=User.objects.create_user(username=username,password=password)
            u.save()
            context={"data":True}
            print(username,password)
            return redirect("login")


    return render(request,"todo/register.html")


@login_required
def tasks(request):
    s=Tasks.objects.filter(user=request.user).values()
    return render(request,"todo/tasks.html",{"s":s})

def addtask(request):
    context={"data":False}
    if request.method=="POST":
        user=request.user
        title=request.POST["title"]
        desc=request.POST["description"]
        s=Tasks(title=title,desc=desc,user=user)
        s.save()
        print(user)
        context={"data":True}

    return render(request,"todo/addtask.html",context)


def deletetask(request,id):
    s=Tasks.objects.get(id=id)
    s.delete()
    return redirect("tasks")

def updatetask(request,id):
    s = Tasks.objects.get(id=id)
    form=TaskForm(instance=s)
    dict={'form':form}
    if request.method=="POST":
        if request.POST.get('title') and request.POST.get('description'):
                Tasks.objects.filter(id = id).update(title= request.POST.get('title'), desc= request.POST.get('description'))
                return redirect("tasks")
    return render(request,"todo/updatetask.html",dict)


def verification(request):
    if request.method=="POST":
        otp=request.POST["otp"]
        print(otp)

    return render(request,"todo/verify.html")


def employee(request,id):
    emp=Tasks.objects.get(id=id)
    return JsonResponse(emp)
