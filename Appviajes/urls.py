from django.urls import path

from Appviajes.views import avion, aviones, colectivo, colectivos, inicio, paquete, paquetes

urlpatterns = [
    path("agrega/avion/<lugar_de_viaje>/<precio>/<hora_vuelo>/<estadia>", avion),
    path("agrega/colectivo/<lugar_de_viaje>/<precio>/<hora_colectivo>/<estadia>", colectivo),
    path("agrega/paquete/<lugar_de_viaje>/<precio>/<hotel_colectivo>/<estadia>", paquete),
    path("aviones/", aviones, name="Aviones"),
    path("colectivos/", colectivos, name="Colectivos"),
    path("paquete/", paquetes, name="Paquetes"),
    path("", inicio, name="Inicio" ),
]
    