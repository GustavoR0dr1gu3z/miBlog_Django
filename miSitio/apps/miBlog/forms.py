from django import forms # Importamos libreria para los formularios

class RegistroForm(forms.Form): # Listos para crear los input del formulario
    username = forms.CharField(required = True, min_length = 4, max_length=60)
    email = forms.EmailField(required = True)
    password = forms.CharField(required = True)
    password2 = forms.CharField(required = True)



