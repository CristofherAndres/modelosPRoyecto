from django.contrib import admin
from modeloApp.models import Persona

# Register your models here.

#Desplegar atributos en el panel admin, y no ver solo un object.
class PersonaAdmin(admin.ModelAdmin):
    list_display = ['id','nombre','correo','telefono']


admin.site.register(Persona, PersonaAdmin)
