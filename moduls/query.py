from django.core.management.base import BaseCommand
from tracking.models import *
from django.core import serializers
import json


def say_hi():
    print("HI")


def get_all():
    g = Tracking.objects.all()
    f = serializers.serialize('json', [x for x in g])
    return json.loads(f)

def saveData(info):
    print(info)
    temp = (info.replace(" ","")).split(";")
    del temp[4:6]
    
    if temp[0]=="ST300STT":
        g = Tracking(Etiqueta =temp[0],
            idSensor=float(temp[1]),
            version =temp[2],
            Software=temp[3],
            CodUbicacion=temp[4],
            Lat =float(temp[5]),
            Lon =float(temp[6]),
            KMH =float(temp[7]),  
            GradosDeRumbo = float(temp[8]) ,
            SatelitesUsados = float(temp[9]),
            GPSCorrecto =int(temp[10]) ,
            DistanciaRecorrida = int(temp[11]),
            VoltajePrincipal = float(temp[12]) ,
            ValorEntradasYsalidas =float(temp[13]),
            Modo = float(temp[14]),
            NumeroReportesEnviados = float(temp[15]),
            ConduccionDeHorasMetros = float(temp[16]), 
            VolInterno = float(temp[17]) ,
            TiempoReal =float(temp[18]) ,
            ValorADC = float(temp[19]),
            )

    elif temp[0]=="ST300ALT":
        g = Tracking(Etiqueta =temp[0],
            idSensor=float(temp[1]),
            version =temp[2],
            Software=temp[3],
            CodUbicacion=temp[4],
            Lat =float(temp[5]),
            Lon =float(temp[6]),
            KMH =float(temp[7]),  
            GradosDeRumbo = float(temp[8]) ,
            SatelitesUsados = float(temp[9]),
            GPSCorrecto =int(temp[10]) ,
            DistanciaRecorrida = int(temp[11]),
            VoltajePrincipal = float(temp[12]) ,
            ValorEntradasYsalidas =float(temp[13]),
            AlertaID=float(temp[14]),
            ConduccionDeHorasMetros = float(temp[15]), 
            VolInterno = float(temp[16]) ,
            TiempoReal =float(temp[17]) ,
            ValorADC = float(temp[18]),
            )
    elif temp[0]=="ST300EMG":
        g = Tracking(Etiqueta =temp[0],
            idSensor=float(temp[1]),
            version =temp[2],
            Software=temp[3],
            CodUbicacion=temp[4],
            Lat =float(temp[5]),
            Lon =float(temp[6]),
            KMH =float(temp[7]),  
            GradosDeRumbo = float(temp[8]) ,
            SatelitesUsados = float(temp[9]),
            GPSCorrecto =int(temp[10]) ,
            DistanciaRecorrida = int(temp[11]),
            VoltajePrincipal = float(temp[12]) ,
            ValorEntradasYsalidas =float(temp[13]),
            Emergencia=float(temp[14]),
            ConduccionDeHorasMetros = float(temp[15]), 
            VolInterno = float(temp[16]) ,
            TiempoReal =float(temp[17]) ,
            ValorADC = float(temp[18]),
            )
    elif temp[0]=="ST300UEX":
        g = Tracking(Etiqueta =temp[0],
            idSensor=float(temp[1]),
            version =temp[2],
            Software=temp[3],
            CodUbicacion=temp[4],
            Lat =float(temp[5]),
            Lon =float(temp[6]),
            KMH =float(temp[7]),  
            GradosDeRumbo = float(temp[8]) ,
            SatelitesUsados = float(temp[9]),
            GPSCorrecto =int(temp[10]) ,
            DistanciaRecorrida = int(temp[11]),
            VoltajePrincipal = float(temp[12]) ,
            ValorEntradasYsalidas =float(temp[13]),
            pasajeros=float(temp[14]),
            ConduccionDeHorasMetros = float(temp[15]), 
            VolInterno = float(temp[16]) ,
            TiempoReal =float(temp[17]) ,
            )
    else:
        g = Tracking(Etiqueta ="Trama no reconocida")
        pass
    
    g.save()
