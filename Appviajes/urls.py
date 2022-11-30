from django.urls import path

from Appviajes.views import busquedaLugar_avion,buscaravion,avion, aviones, colectivo, colectivos, inicio, paquete, paquetes
from Appviajes.views import AvionList,AvionCreate,AvionUpdate,AvionDelete,AvionDetail

urlpatterns = [
    path("agrega/avion/<lugar_de_viaje>/<precio>/<hora_vuelo>/<estadia>", avion),
    path("agrega/colectivo/<lugar_de_viaje>/<precio>/<hora_colectivo>/<estadia>", colectivo),
    path("agrega/paquete/<lugar_de_viaje>/<precio>/<hotel_colectivo>/<estadia>", paquete),
    path("aviones/", aviones, name="Aviones"),
    path("colectivos/", colectivos, name="Colectivos"),
    path("paquete/", paquetes, name="Paquetes"),
    path("", inicio, name="Inicio" ),
    #busqueda lugar avion
    path("busquedaLugar_avion/", busquedaLugar_avion, name="busquedaLugar_avion" ),
    path('buscaravion/',buscaravion, name="buscaravion"),
    #CRUD avion
    path('listaAvion/', AvionList.as_view(), name="ListaAviones"),
    path('detalleAvion/<pk>', AvionDetail.as_view(), name="DetalleAvion"),
    path('creaAvion/', AvionCreate.as_view(), name="CreaAviones"),
    path('actualizarAvion/<pk>', AvionUpdate.as_view(), name="ActualizaAviones"),
    path('eliminarAvion/<pk>', AvionDelete.as_view(), name="EliminaAviones"),
]
    