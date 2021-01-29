from django.shortcuts import render, HttpResponse, redirect #4.1 .-  se importa redirect, para redireccionar a una pagina si el usuario existe
from django.contrib.auth import authenticate, login, logout #4.-  Se importa la autenticacion y el login
from django.contrib import messages #Para mostrar mensajes

# Create your views here.
def index(request): #Creando una funcion que muestra lo que queremos en la pagina principal
    return render(request,'index.html',{
        'mensaje': 'Hecho Por Gustavo Calzada', #Informacion
    })


def ingresar(request): #2.- Ya que creamos la URL, creamos el metodo que le creamos desde URL, y recibe request y nuestro template (login.html)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST .get('password') # 3.- El if se usa porque estamos ocupando POST, y recibimos los datos de username y password, de nuestro template login.html

        user = authenticate(username=username, password = password) #Se valida el usuario, el dato a la derecha es la variable que se declaró arriba

        if user: #Si existe el usuario entonces se va a loggear 
            login(request, user)
            messages.success(request,'Bienvenido {}'.format(user.username)) # Mensaje
            return redirect('index') # Se va a redireccionar a index
        else:
            messages.error(request, 'Usuario o Contraseña Incorrecta') # Mensaje

    return render(request, 'login.html', {
    
    })    


def salir(request): # Creando funcion que hace que terminemos la sesion
    logout(request)
    messages.success(request, 'Sesion Finalizada')
    return redirect('ingresar')

def registrou(request):        
    return render(request,'registro.html', {
        
    })






