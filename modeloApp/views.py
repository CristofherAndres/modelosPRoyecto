from django.shortcuts import render
from modeloApp.models import Persona

# Create your views here.
def personasData(request):
    #sql -> select * from tabla;
    personas = Persona.objects.all()
    data = {'personas': personas}
    return render(request, 'modeloApp/formPersonas.html', data)