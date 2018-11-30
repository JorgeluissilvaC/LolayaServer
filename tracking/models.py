from django.db import models
from django.utils import timezone

class Tracking(models.Model):

	Etiqueta = models.CharField(max_length=200,blank=True)
	idSensor = models.BigIntegerField(null=True)
	interno = models.CharField(max_length=200,blank=True)
	placa = models.CharField(max_length=200,blank=True)
	version = models.CharField(max_length=200,blank=True)
	Software = models.CharField(max_length=200,blank=True)
	date = models.DateTimeField(default=timezone.now,null=True)
	Lat = models.DecimalField(max_digits=10, decimal_places=8,null=True)
	Lon = models.DecimalField(max_digits=10, decimal_places=8,null=True)
	KMH = models.DecimalField(max_digits=10, decimal_places=8,null=True)
	GradosDeRumbo =  models.DecimalField(max_digits=5, decimal_places=2,null=True)
	VoltajePrincipal =  models.DecimalField(max_digits=10, decimal_places=2,null=True)
	Modo = models.BigIntegerField(null=True)
	IdGeocerca = models.BigIntegerField(null=True)
	Emergencia = models.BigIntegerField(null=True)
	AlertaID = models.BigIntegerField(null=True)
	pasajeros = models.BigIntegerField(null=True)
	VolInterno =  models.DecimalField(max_digits=10, decimal_places=2,null=True)