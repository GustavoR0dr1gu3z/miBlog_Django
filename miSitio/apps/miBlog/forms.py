from django import forms # Importamos libreria para los formularios
from django.contrib.auth.models import User # Clase por defecto que tiene Django


class RegistroForm(forms.Form): # Listos para crear los input del formulario
    username = forms.CharField(label = 'Nombre de Usuario', required = True, min_length = 4, max_length=60, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                                                            'placeholder': 'Nombre de Usuario'}))
    email = forms.EmailField(label = 'Correo Electrónico', required = True, widget=forms.EmailInput(attrs={'class': 'form-control',
                                                                            'placeholder': 'hola@ejemplo.com'}))
    password = forms.CharField(label = 'Contraseña', required = True, widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                                'placeholder': 'Password'}))
    password2 = forms.CharField(label = 'Repetir Contraseña', required = True,  widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                                'placeholder': 'Repeat Password'}))

    def clean_username(self): # Metodo para validacion 
        username = self.cleaned_data.get('username') # consulta para verificar si existe el nombre de usuario
        if(User.objects.filter(username=username).exists()):
            raise forms.ValidationError('Nombre de Usuario en Uso')
        return username

    def clean_email(self): # Metodo para validacion 
        email = self.cleaned_data.get('email') # consulta para verificar si existe el nombre de usuario
        if(User.objects.filter(email=email).exists()):
            raise forms.ValidationError('Correo Electrónico en Uso')
        return email

    def clean(self):
        cleaned_data = super().clean() # cleaned_data se ocupa cuando los campos dependen uno del otro
        if cleaned_data.get('password2') != cleaned_data.get('password'):
            self.add_error('password2', 'La Contraseña no Coincide')




