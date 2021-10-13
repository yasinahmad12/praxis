from django.http import request
from django.shortcuts import redirect, render

from . import models

# Create your views here.
def index (req):
    return render(req, 'home.html')

def input_makan (req):
    if req.POST:
        models.lapar.objects.create(
            jenis= req.POST['jenis'],
            nama= req.POST['nama'],
            harga= req.POST['harga'],
            
        )
        return redirect('/foods/')
    cemilan= models.lapar.objects.all()
    return render(req, 'makanan.html',{
        'data_makan': cemilan,
    })
def input_minuman (req):
    if req.POST:
        models.lapar.objects.create(
            jenis= req.POST['jenis'],
            nama= req.POST['nama'],
            harga= req.POST['harga'],
            
        )
        return redirect('/foods/')
    cemilan= models.lapar.objects.all()
    return render(req, 'minuman.html',{
        'data_minum': cemilan,
    })


def hapus (req, id) :
    models.lapar.objects.filter(pk=id).delete()
    return redirect('/foods')

def menu_utama (req):
    menu = models.lapar.objects.all()
    return render(req,"home.html",{
        'menu': menu
    })
