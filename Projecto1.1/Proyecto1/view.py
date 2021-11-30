from django.http import HttpResponse
from django.template import Template, Context
import os

d = "/".join(os.getcwd().split("\\"))

def estadisticas_generales(request):
  with open(d + "/Proyecto1/plantilas/estadisticas_general.html") as Documento_Ext:
    Plantilla = Template(Documento_Ext.read())
  Documento_Ext.close()
  return HttpResponse(Plantilla.render(Context()))

def regiones(request):
  with open(d + "/Proyecto1/plantilas/regiones.html") as Documento_Ext:
    Plantilla = Template(Documento_Ext.read())
  Documento_Ext.close()
  return HttpResponse(Plantilla.render(Context()))