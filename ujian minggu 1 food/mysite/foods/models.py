from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class makan (models.Model) :
    jenis = models.CharField (default ='', max_length= 30)
    nama = models.CharField (default ='' ,max_length= 30)
    harga = models.IntegerField()

class minum (models.Model) :
    jenis = models.CharField (default ='', max_length= 30)
    nama = models.CharField (default ='' ,max_length= 30)
    harga = models.IntegerField()

class home (models.Model) :
    namamakan = models.ForeignKey(makan, on_delete=CASCADE, related_name='makanan')
    namaminuman = models.ForeignKey(makan, on_delete=CASCADE, related_name='minuman')