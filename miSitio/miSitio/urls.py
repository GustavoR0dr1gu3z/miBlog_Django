"""miSitio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from apps.miBlog import views # Importando la vista de miBlog

urlpatterns = [    
    path('usuarios/salir',views.salir, name="salir"),
    path('usuarios/ingresar',views.ingresar, name="ingresar"), # 1.- Crear URL, donde queremos que la ruta se ingrese 127.0.0.1:8000/usuarios/ingresar    
    path('',views.index, name="index"), # Llamar la funcion que se creo en views
    path('admin/', admin.site.urls),
]
