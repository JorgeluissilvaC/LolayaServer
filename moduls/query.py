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
    
    temp = (info.replace(" ","")).split(";")
    print(info)
    print("Esta")
    del temp[4:6]
    
    if temp[0]=="ST300STT":
        g = Tracking(Etiqueta =temp[0],
            idSensor=float(temp[1]),
            interno = " ",
            placa = " ",
            version =temp[2],
            Software=temp[3],
            Lat =float(temp[5]),
            Lon =float(temp[6]),
            KMH =float(temp[7]),  
            GradosDeRumbo = float(temp[8]) ,
            VoltajePrincipal = float(temp[12]) ,
            Modo = float(temp[14]),
            VolInterno = float(temp[17]) ,
            )

    elif temp[0]=="ST300ALT":
        g = Tracking(Etiqueta =temp[0],
            idSensor=float(temp[1]),
            interno = " ",
            placa = " ",
            version =temp[2],
            Software=temp[3],
            Lat =float(temp[5]),
            Lon =float(temp[6]),
            KMH =float(temp[7]),  
            GradosDeRumbo = float(temp[8]) ,
            VoltajePrincipal = float(temp[12]) ,
            AlertaID=float(temp[14]),
            VolInterno = float(temp[16]) ,
            )
    elif temp[0]=="ST300EMG":
        g = Tracking(Etiqueta =temp[0],
            idSensor=float(temp[1]),
            interno = " ",
            placa = " ",
            version =temp[2],
            Software=temp[3],
            Lat =float(temp[5]),
            Lon =float(temp[6]),
            KMH =float(temp[7]),  
            GradosDeRumbo = float(temp[8]) ,
            VoltajePrincipal = float(temp[12]) ,
            Emergencia=float(temp[14]),
            VolInterno = float(temp[16]) ,
            )
    elif temp[0]=="ST300UEX":
        g = Tracking(Etiqueta =temp[0],
            idSensor=float(temp[1]),
            interno = " ",
            placa = " ",
            version =temp[2],
            Software=temp[3],
            Lat =float(temp[5]),
            Lon =float(temp[6]),
            KMH =float(temp[7]),  
            GradosDeRumbo = float(temp[8]) ,
            VoltajePrincipal = float(temp[12]) ,
            pasajeros=float(temp[14]),
            VolInterno = float(temp[16]) ,
            )
    else:
        g = Tracking(Etiqueta ="Trama no reconocida")
        pass
    
    g.save()
