from django.shortcuts import render
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('p-c11', views.pj, name="class 11 physics"),
    path('m-c11', views.mj, name="class 11 maths"),
    path('c-11', views.cj, name="class 11 chemistry"),
    path('p-12', views.ps, name="class 12 physics"),
    path('c-12', views.cs, name="class 12 chemistry"),
    path('m-12', views.ms, name="class 12 maths")

]