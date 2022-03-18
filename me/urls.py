
from django.contrib import admin
from django.urls import path, include
from .views import Home, Contact
urlpatterns = [
   
    path("", Home,name="home"),
    path("contact/", Contact,name="contact"),
   
]
