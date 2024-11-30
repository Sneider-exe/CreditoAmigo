from django import forms
from .models import Reserva

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control letra-kanit-300'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control letra-kanit-300'}))

class RegistroForm(forms.Form):
    nombre = forms.CharField(label='Nombre', max_length=100)
    fecha_nacimiento = forms.DateField(label='Fecha de Nacimiento')
    cedula = forms.IntegerField(label='Cedula')
    email = forms.EmailField(label='Correo Electrónico')
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)

    # Nuevo campo para el nombre de usuario
    username = forms.CharField(label='Usuario', max_length=100)

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['fecha_llegada', 'matricula_vehiculo', 'tiempo_requerido', 'necesita_restaurante', 'necesita_mantenimiento']
        widgets = {
            'fecha_llegada': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'hora_llegada': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}), # 'readonly': True}),
            'matricula_vehiculo': forms.TextInput(attrs={'class': 'form-control'}),
            'tiempo_requerido': forms.NumberInput(attrs={'class': 'form-control'}),
            'necesita_restaurante': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'necesita_mantenimiento': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class HistorialReservasForm(ReservaForm):
    class Meta:
        model = Reserva
        fields = ['fecha_llegada', 'matricula_vehiculo', 'tiempo_requerido', 'necesita_restaurante', 'necesita_mantenimiento', 'estado']
        widgets = {
            'fecha_llegada': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'readonly': True}),
            'matricula_vehiculo': forms.TextInput(attrs={'class': 'form-control', 'readonly': True}),
            'tiempo_requerido': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True}),
            'necesita_restaurante': forms.CheckboxInput(attrs={'class': 'form-check-input', 'disabled': True}),
            'necesita_mantenimiento': forms.CheckboxInput(attrs={'class': 'form-check-input', 'disabled': True}),
            'estado': forms.TextInput(attrs={'class': 'form-control', 'readonly': True}),
        }