from django.urls import include, path
from . import views
from django.contrib import admin


urlpatterns = [
    path('arealoc', views.arealoc, name='arealoc'),
    path('annanagar', views.annanagar, name='annanagar'),
    path('theppakulam', views.theppakulam, name='theppakulam'),
    path('villapuram', views.villapuram, name='villapuram') 

]