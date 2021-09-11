from main.models import Viaje, User
from django.contrib import messages
from django.shortcuts import redirect, render
import bcrypt
from .decorators import login_required
from main.auth import User


@login_required
def home(request):
    viajes = Viaje.objects.all()
    usuarios = User.objects.all() 
    user_id = int(request.session['user']['id'])
    mis_viajes = Viaje.objects.filter( owner_user_id = user_id)
    otros_viajes = Viaje.objects.exclude(owner_user_id = user_id)
    one_user = User.objects.get(id = user_id)
    viaje_de_otros = one_user.viajes.all()
    context = {
        'viajes': mis_viajes,
        'otros' : otros_viajes,
        'de_otros' : viaje_de_otros
    }
    return render(request, 'index.html', context)


@login_required
def create(request):
    if request.method == "GET":
        return render(request,"create.html")

    if request.method == "POST":
        destination = request.POST['destination']
        travel_star = request.POST['star']
        travel_end = request.POST['end']
        plan = request.POST['plan']
        user_id = int(request.session['user']['id'])
        new_plan = Viaje.objects.create(
            destination = destination, travel_star = travel_star, travel_end = travel_end,
            plan=plan, owner_user_id = user_id)
    return redirect("/")

@login_required
def view(request, viaje_id):
    viaje = Viaje.objects.get(id = viaje_id)
    #viajeros = Viaje.objects.all().exclude(id = viaje.owner_user.id)
    context = {
        'viaje' : viaje,
        #'viajeros': viajeros
    }
    return render(request,"datos.html", context)


@login_required
def join(request, viaje_id):
    user_id = int(request.session['user']['id'])
    user = User.objects.get(id = user_id)
    viaje = Viaje.objects.get(id = viaje_id)
    user.viajes.add(viaje)
    return redirect(request.META.get('HTTP_REFERER'))
