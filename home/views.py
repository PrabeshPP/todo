from django.shortcuts import render,redirect
from .models import Tasks

# Create your views here.

def home(request):
    tasks=Tasks.objects.all()
    return render(request,'home/home.html',{'tasks':tasks})

def add(request):
    if(request.method=="POST"):
        title=request.POST["title"]
        description=request.POST['description']
        task=Tasks.objects.create(title=title,description=description)
        task.save()
        return redirect('/')
    return render(request,'home/add.html')
