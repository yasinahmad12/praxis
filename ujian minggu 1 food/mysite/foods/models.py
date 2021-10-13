from django.db import models

# Create your models here.
class lapar (models.Model) :
    jenis = models.CharField (default ='', max_length= 30)
    nama = models.CharField (default ='' ,max_length= 30)
    harga = models.IntegerField()