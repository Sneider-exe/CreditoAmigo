from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import *
from .models import Reserva


def profile_view(request):
    # Lógica para la vista de perfil aquí
    return render(request, 'account/profile.html')  # Ajusta la plantilla según tus necesidades

def registro_view(request):
    logout(request)
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            # Procesar el formulario de registro
            nombre = form.cleaned_data['nombre']
            fecha_nacimiento = form.cleaned_data['fecha_nacimiento']
            cedula = form.cleaned_data['cedula']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            username = form.cleaned_data['username']

            # Crear nuevo usuario con el nombre proporcionado como nombre de usuario
            new_user = User.objects.create_user(username=username, password=password)
            new_user.email = email
            new_user.first_name = nombre
            new_user.last_name = nombre
            new_user.date_joined = fecha_nacimiento
            # Ajusta otras propiedades del usuario según sea necesario

            new_user.save()

            # Autenticar al usuario recién creado
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')  # Redirigir a la página principal después de registrarse
    else:
        form = RegistroForm()

    return render(request, 'account/registro.html', {'form': form})

def user_login(request):
    logout(request)
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, 
                                 username=cd['username'], 
                                 password=cd['password'] )
            if user is not None:
                if user.is_active:
                    login(request, user)
                    template = loader.get_template('reserva.html')
                    context = {}
                    return HttpResponse(template.render(context, request))
                else:
                    return HttpResponse('El usuario no esta activo')
            else:
                return HttpResponse('Usuario o contraseña invalido')
    else:
        form = LoginForm()
        return render(request, 'account/login.html', {'form': form})

def index(request):
    logout(request)
    template = loader.get_template('index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def logout_view(request):
    logout(request)
    request.session.flush()
    return redirect('index')  # Cambia 'index' por la URL a la que deseas redirigir al usuario después de cerrar sesión

@login_required  # Agrega esta decoración si deseas que solo usuarios autenticados puedan acceder a esta vista
def crear_reserva(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            reserva = form.save(commit=False)
            reserva.usuario = request.user 
            reserva.fecha_llegada = form.cleaned_data['fecha_llegada']
            reserva.necesita_restaurante = form.cleaned_data['necesita_restaurante']
            reserva.necesita_mantenimiento = form.cleaned_data['necesita_mantenimiento']
            reserva.estado = 'completada'
            reserva.save()
            return redirect('historial')
    else:
        form = ReservaForm()

    return render(request, 'reserva.html', {'form': form})

@login_required
def historial_reservas(request):
    reservas = Reserva.objects.filter(usuario=request.user, estado='completada')
    form = HistorialReservasForm()

    return render(request, 'HistorialReservas.html', {'reservas': reservas, 'form': form})