from django.http import HttpResponse
from django.template import Template, Context
import os

d = "/".join(os.getcwd().split("\\"))

def estadisticas_generales(request):
  with open(d + "/Proyecto1/plantilas/Estadisticas_Generales.html") as Documento_Ext:
    Plantilla = Template(Documento_Ext.read())
  Documento_Ext.close()
  return HttpResponse(Plantilla.render(Context()))

def regiones(request):
  with open(d + "/Proyecto1/plantilas/Selección_Regional.html") as Documento_Ext:
    Plantilla = Template(Documento_Ext.read())
  Documento_Ext.close()
  return HttpResponse(Plantilla.render(Context()))



# Parte de regiones:

def XV_Arica(request):
  with open(d + "/Proyecto1/regiones/XV - Arica y Parinacota.html") as Documento_Ext:
    Plantilla = Template(Documento_Ext.read())
  Documento_Ext.close()
  return HttpResponse(Plantilla.render(Context()))


#JSON
def DataProduct4(request):
  with open(d + "/API/json/DP4.json") as Documento_Ext:
    Plantilla = Template(Documento_Ext.read())
  Documento_Ext.close()
  return HttpResponse(Plantilla.render(Context()))
def DataProduct5(request):
  with open(d + "/API/json/DP5.json") as Documento_Ext:
    Plantilla = Template(Documento_Ext.read())
  Documento_Ext.close()
  return HttpResponse(Plantilla.render(Context()))
def DataProduct7(request):
  with open(d + "/API/json/DP7.json") as Documento_Ext:
    Plantilla = Template(Documento_Ext.read())
  Documento_Ext.close()
  return HttpResponse(Plantilla.render(Context()))
