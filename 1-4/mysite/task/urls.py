from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<id>/hapus', views.hapus),
    path('<id>/detail', views.detail),
    path('<id>/edit', views.edit),

]