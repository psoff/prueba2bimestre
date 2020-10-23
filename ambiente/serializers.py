from app.models import *
from rest_framework import serializers

class PersonaSerializers(serializers.ModelSerializer):
    class Meta:
        model=Persona
        fields= ('nombre','cedula','ciudad','direccion','telefono')

class LugarSerializers(serializers.ModelSerializer):
    class Meta:
        model=Lugar
        fields=('nombre','area','ciudad','direccion','encargado')

class EventoSerializers(serializers.ModelSerializer):
    class Meta:
        model=Eventos
        fields= ('nombre','lugar','ciudad','hora','url')    
          