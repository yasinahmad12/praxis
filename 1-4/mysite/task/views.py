from django.shortcuts import redirect, render

# Create your views here.
from . import models
# from mysite import task 

def index(request):
    if request.POST:
       models.Ahai.objects.create(name=request.POST['name'])
       return redirect("/")
    
    tasks = models.Ahai.objects.all()
    return render (request,"home/index.html",{
        "data": tasks
    })

def hapus (request,id):
    models.Ahai.objects.filter(pk = id).delete()
    return redirect('/')

def detail (request,id):
    data = models.Ahai.objects.filter(pk = id).first()
    print(data)
    return render(request, 'Detail.html',{
        'dataDetail' : data
    })

def edit (request,id):
    if request.POST:
        input = request.POST['nama']
        print(input)
        models.Ahai.objects.filter(pk = id).update(name = input)
        return redirect('/')
    data2 = models.Ahai.objects.filter(pk = id).first()
    print(data2)
    return render (request,'edit.html', {
        "Detailedit" : data2,
    })