from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request): #Creando una funcion que muestra lo que queremos en la pagina principal
    return HttpResponse("<h1>Holaaa</h1>")