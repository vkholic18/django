from django.shortcuts import render
from django.http import HttpResponse
from home.models import Contact

# Create your views here.
def home(request):
    context={'name':'SaiTeja','Age':22}
    return render(request,"home.html",context)


def projects(request):
    return render(request,"projects.html")

def about(request):
    return render(request,"about.html")

def contact(request):
    if request.method=="POST":
        name=request.POST['name1']
        email=request.POST['email']
        description=request.POST['description']
        contact=request.POST['contactno']
        print(name,email,description,contact)
        ins=Contact(name=name,email=email,description=description,contact=contact)
        ins.save()
    return render(request,"contact.html")
