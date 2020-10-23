from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
from rest_framework import viewsets
from ambiente.serializers import PersonaSerializers,LugarSerializers,EventoSerializers
# Create your views here.
class PersonaViewSet(viewsets.ModelViewSet ):
    queryset = Persona.objects.all().order_by('nombre')
    serializer_class = PersonaSerializers

class LugarViewSet(viewsets.ModelViewSet ):
    queryset = Lugar.objects.all().order_by('nombre')
    serializer_class = LugarSerializers

class EventoViewSet(viewsets.ModelViewSet ):
    queryset = Eventos.objects.all().order_by('nombre')
    serializer_class = EventoSerializers  

def index (request):
    return HttpResponse("Esta es una pagina que puede ayudar a conectar ecologistas de todo el pais para entre ellos capacitarse en normas ecologistas, o para reunirse en lugar en los que sea necesario reactivar la ecologia ya sea plantando arboles, o insertando especies")
