from django.contrib import admin
from . models import Persona
from . models import Lugar
from . models import Eventos

# Register your models here.
admin.site.register(Persona)
admin.site.register(Lugar)
admin.site.register(Eventos)
