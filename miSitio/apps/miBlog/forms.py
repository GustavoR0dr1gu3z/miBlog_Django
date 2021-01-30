from django import forms # Importamos libreria para los formularios

class RegistroForm(forms.Form): # Listos para crear los input del formulario
    username = forms.CharField(label = 'Nombre de Usuario', required = True, min_length = 4, max_length=60, widget=forms.TextInput(attrs={'class': 'form-control',
                                                                                                            'placeholder': 'Nombre de Usuario'}))
    email = forms.EmailField(label = 'Correo Electrónico', required = True, widget=forms.EmailInput(attrs={'class': 'form-control',
                                                                            'placeholder': 'hola@ejemplo.com'}))
    password = forms.CharField(label = 'Contraseña', required = True, widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                                'placeholder': 'Password'}))
    password2 = forms.CharField(label = 'Repetir Contraseña', required = True,  widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                                'placeholder': 'Repeat Password'}))



