from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name="home"),
    path('', views.home, name="home"),
    path('download/', views.download, name="download"),
    path('about/', views.about, name="about"),
    path('docs/', views.docs, name="docs"),
    path('basic_first_aid/', views.basic_first_aid, name="basic_first_aid"),
    path('test/', views.test, name="test"),
]