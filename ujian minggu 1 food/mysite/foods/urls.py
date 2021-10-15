from django import urls
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('foods/', views. input_makan),
    path('drink/', views. input_minuman),
    path('makan/hapus/<id>', views.hapus_makan),
    path('minum/hapus/<id>', views.hapus_minum),

]