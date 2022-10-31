from django.contrib import admin

from .models import Avion, Colectivo, Paquete

# Register your models here.
admin.site.register(Paquete)
admin.site.register(Avion)
admin.site.register(Colectivo)

