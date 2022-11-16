from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name="home"),
    path('', views.home, name="home"),
    path('download/', views.download, name="download"),
    path('about/', views.about, name="about"),
    path('test/', views.test, name="test"),
]