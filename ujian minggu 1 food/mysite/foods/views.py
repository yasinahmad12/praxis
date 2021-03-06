from django.http import request
from django.shortcuts import redirect, render

from . import models

# Create your views here.
def index (req): 
    menu_utama = models.home.objects.all() 
    data_makanan= models.makan.objects.all()
    data_minuman= models.minum.objects.all()

    return render(req, 'indexhome/home.html',{
        'data': menu_utama,
        'data1': data_makanan,
        'data2': data_minuman,
    })

def input_makan (req):
    if req.POST:
        models.makan.objects.create(
            jenis= req.POST['jenis'],
            nama= req.POST['nama'],
            harga= req.POST['harga'],
            
        )
        return redirect('/foods/')
    cemilan= models.makan.objects.all()
    return render(req, 'indexmakan/makanan.html',{
        'data_makan': cemilan,
    })
def input_minuman (req):
    if req.POST:
        models.minum.objects.create(
            jenis= req.POST['jenis'],
            nama= req.POST['nama'],
            harga= req.POST['harga'],
            
        )
        return redirect('/drink/')
    cemilan= models.minum.objects.all()
    return render(req, 'indexminum/minuman.html',{
        'data_minum': cemilan,
    })


def hapus_makan (req, id) :
    models.makan.objects.filter(pk=id).delete()
    return redirect('/foods/')


def hapus_minum (req, id) :
    models.minum.objects.filter(pk=id).delete()
    return redirect('/drink/')