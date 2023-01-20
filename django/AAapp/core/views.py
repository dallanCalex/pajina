from django.shortcuts import render, HttpResponse 

html_base ="""
<h1> METODO DE PAGO</h1>
<ul>
    <li><a href="/">Portada</a></li>
    <li><a href="/login/">Iniciar secion</a></li>
    <li><a href="/registro/">Crear cuenta nueva</a></li>
    <li><a href="/tarjeta/">AÑADIR TARJETA</a></li>
    <li><a href="/index/"></a></li>
"""
# Create your views here.


def home(request):
    return render(request, "core/home.html")


def login(request):
    return render(request, "core/login.html")


def registro(request):
    return render(request, "core/registro.html")


def index(request):
    return render(request, "core/index.html")
    
def tarjeta(request):
    return render(request, "core/tarjeta.html")