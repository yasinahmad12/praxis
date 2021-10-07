from django.shortcuts import redirect, render

# Create your views here.
from . import models 

def index(request):
    if request.POST:
       models.Ahai.objects.create(name=request.POST['name'])
       return redirect("/")
    
    tasks = models.Ahai.objects.all()
    return render (request,"home/index.html",{
        "data": tasks
    })