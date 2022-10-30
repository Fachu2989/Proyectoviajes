from django.db import models


# Create your models here.
class Avion(models.Model):
    lugar_de_viaje = models.CharField(max_length=50)
    precio = models.IntegerField()
    hora_vuelo= models.IntegerField()
    estadia = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.lugar_de_viaje} - {self.precio} - {self.hora_vuelo} - {self.estadia}"

class Colectivo(models.Model):
    lugar_de_viaje = models.CharField(max_length=50)
    precio = models.IntegerField()
    hora_colectivo= models.IntegerField()
    estadia = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.lugar_de_viaje} - {self.precio} - {self.hora_colectivo} - {self.estadia}"

class Paquete(models.Model):
    lugar_de_viaje = models.CharField(max_length=50)
    hotel_colectivo = models.CharField(max_length=50)
    precio= models.IntegerField()
    estadia = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.lugar_de_viaje} - {self.hotel_colectivo} - {self.precio} - {self.estadia}"