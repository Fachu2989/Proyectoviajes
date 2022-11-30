from django.shortcuts import render
from .models import Avion, Colectivo, Paquete
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


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


#Busqueda Aviones
def busquedaLugar_avion(request):
    return render (request, 'busquedaLugar_avion.html')

def buscaravion(request):
    lugar_buscada= request.GET['lugar_de_viaje']
    avion= Avion.objects.get(lugar_de_viaje=lugar_buscada)
    return render(request,'resultado_busqueda_avion.html',{"avion":avion, "lugar_de_viaje": lugar_buscada})

#CRUD vista basada en clase (curso)
class AvionList(ListView):

    model = Avion
    template_name = 'avion_list.html'
    context_object_name = "Aviones"

class AvionDetail(DetailView):

    model = Avion
    template_name = 'avion_detail.html'
    context_object_name = "avion"

class AvionCreate(CreateView):

    model = Avion
    template_name = 'avion_create.html'
    fields = ('__all__')
    success_url = '/viajes/'

class AvionUpdate(UpdateView):

    model = Avion
    template_name = 'avion_update.html'
    fields = ('__all__')
    success_url = '/viajes/'

class AvionDelete(DeleteView):

    model = Avion
    template_name = 'avion_delete.html'
    success_url = '/viajes/'
 