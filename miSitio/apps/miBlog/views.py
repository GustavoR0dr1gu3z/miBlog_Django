from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request): #Creando una funcion que muestra lo que queremos en la pagina principal
    return render(request,'index.html',{
        'mensaje': 'Hecho Por Gustavo Calzada', #Informacion
    })


def ingresar(request): #2.- Ya que creamos la URL, creamos el metodo que le creamos desde URL, y recibe request y nuestro template (login.html)
    return render(request, 'login.html', {

    })    