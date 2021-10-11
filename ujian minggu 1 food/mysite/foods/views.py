from django.http import request
from django.shortcuts import redirect, render

from mysite.foods import models

# Create your views here.
def index (req):
    return render(req, 'home.html')

def input (req):
    if req.POST:
        models.Lapar.objects.create(
            jenis= req.POST['jenis'],
            nama= req.POST['nama'],
            harga= req.POST['harga'],
            
        )
        return redirect('/')
    cemilan= models.Lapar.objects.all()
    return render(req, 'input.html',{
        'data_makan': cemilan,
    })