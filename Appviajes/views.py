from django.shortcuts import render
from .models import Avion, Colectivo, Paquete
from django.http import HttpResponse
# Create your views here.
def avion(request, lugar_de_viaje, precio,hora_vuelo,estadia):

    avion=Avion(lugar_de_viaje=lugar_de_viaje,precio=precio,hora_vuelo=hora_vuelo, estadia=estadia)
    avion.save()

    return  HttpResponse(f""" 
        <p> Avion a {avion.lugar_de_viaje} con precio de {avion.precio} las horas de vuelo son de {avion.hora_vuelo} y los dias de estadia son {avion.estadia} se a agregado correctamente </p>
    """)

def colectivo(request, lugar_de_viaje, precio,hora_colectivo,estadia):

    colectivo=Colectivo(lugar_de_viaje=lugar_de_viaje,precio=precio,hora_colectivo=hora_colectivo, estadia=estadia)
    colectivo.save()

    return  HttpResponse(f""" 
        <p> colectivo a {colectivo.lugar_de_viaje} con precio de {colectivo.precio} las horas en colectivo son de {colectivo.hora_colectivo} y los dias de estadia son {colectivo.estadia} se a agregado correctamente </p>
    """)

def paquete(request, lugar_de_viaje, precio,hotel_colectivo,estadia):

    paquete=Paquete(lugar_de_viaje=lugar_de_viaje,precio=precio,hotel_colectivo=hotel_colectivo, estadia=estadia)
    paquete.save()

    return  HttpResponse(f""" 
        <p> El Paquete a {paquete.lugar_de_viaje} con precio de {paquete.precio} el hotel del Paquete es {paquete.hotel_colectivo} y los dias de estadia son {paquete.estadia} se a agregado correctamente </p>
    """)


def inicio(request):
    return render(request,"inicio.html")
    
def aviones(request):
    lista=Avion.objects.all()
    return render(request,"aviones.html", {"lista_aviones":lista})

def colectivos(request):
    lista=Colectivo.objects.all()
    return render(request,"colectivos.html", {"lista_colectivos":lista})

def paquetes(request):
    lista=Paquete.objects.all()
    return render(request,"paquetes.html", {"lista_paquetes":lista})
