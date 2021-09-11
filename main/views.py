from main.models import User, Viajeros,Viaje
from django.contrib import messages
from django.shortcuts import redirect, render
import bcrypt
from .decorators import login_required


@login_required
def home(request):
    viajes = Viaje.objects.all() 

    context = {
        'viajes': viajes
    }
    return render(request, 'index.html', context)

def create(request):
    pass


