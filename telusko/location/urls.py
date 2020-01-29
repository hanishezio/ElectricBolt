from django.urls import include, path
from . import views
from django.contrib import admin


urlpatterns = [
    path('location', views.location, name='location'),
    path('homepage', views.homepage, name='homepage'),      

]