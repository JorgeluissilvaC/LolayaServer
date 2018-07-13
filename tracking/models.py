from django.db import models
from django.utils import timezone

class Tracking(models.Model):

	Etiqueta = models.CharField(max_length=200,blank=True)
	idSensor = models.BigIntegerField(null=True)
	version = models.CharField(max_length=200,blank=True)
	Software = models.CharField(max_length=200,blank=True)
	date = models.DateTimeField(default=timezone.now,null=True)
	CodUbicacion = models.CharField(max_length=200,blank=True)
	Lat = models.DecimalField(max_digits=10, decimal_places=8,null=True)
	Lon = models.DecimalField(max_digits=10, decimal_places=8,null=True)
	KMH = models.DecimalField(max_digits=10, decimal_places=8,null=True)
	GradosDeRumbo =  models.DecimalField(max_digits=5, decimal_places=2,null=True)
	SatelitesUsados = models.BigIntegerField(null=True)
	GPSCorrecto = models.BigIntegerField(null=True)
	DistanciaRecorrida = models.DecimalField(max_digits=10, decimal_places=2,null=True)
	VoltajePrincipal =  models.DecimalField(max_digits=10, decimal_places=2,null=True)
	ValorEntradasYsalidas =  models.DecimalField(max_digits=10, decimal_places=2,null=True)
	Modo = models.BigIntegerField(null=True)
	IdGeocerca = models.BigIntegerField(null=True)
	NumeroReportesEnviados = models.BigIntegerField(null=True)
	Emergencia = models.BigIntegerField(null=True)
	AlertaID = models.BigIntegerField(null=True)
	pasajeros = models.BigIntegerField(null=True)
	ConduccionDeHorasMetros =  models.DecimalField(max_digits=10, decimal_places=2,null=True)
	VolInterno =  models.DecimalField(max_digits=10, decimal_places=2,null=True)
	TiempoReal = models.BigIntegerField(null=True)
	ValorADC = models.DecimalField(max_digits=10, decimal_places=2,null=True)

# Create your models here.
