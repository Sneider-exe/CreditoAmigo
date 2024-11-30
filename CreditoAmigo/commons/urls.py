from django.urls import path
from .views import *

urlpatterns = [
    path('login/', user_login, name='login'), 
    path('logout/', logout_view, name='logout'),
    path('accounts/profile/', profile_view, name='profile'), 
    path('registro/', registro_view, name='registro'),
    path('accounts/profile/', profile_view, name='profile'),
    path('reserva/', crear_reserva, name='reserva'),
    path('historial/', historial_reservas, name='historial'),
    path('', index, name='index'),  

]
