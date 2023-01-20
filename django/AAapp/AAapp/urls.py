
from django.contrib import admin
from django.urls import path
from core import views 

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.login, name="login"),
    path('registro/', views.registro, name="registro"),
    path('index/', views.index, name="index"),
    path('tarjeta/', views.tarjeta, name="tarjeta"),

    path('admin/', admin.site.urls)
]