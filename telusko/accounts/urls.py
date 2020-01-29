from django.urls import include, path
from . import views
from django.contrib import admin


urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('index', views.index, name='index'),
    path('logout', views.logout, name='logout')

]