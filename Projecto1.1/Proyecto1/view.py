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



# Regiones:
def XV_Arica(request):
  with open(d + "/Proyecto1/regiones/XV - Arica y Parinacota.html") as Documento_Ext:
    Plantilla = Template(Documento_Ext.read())
  Documento_Ext.close()
  return HttpResponse(Plantilla.render(Context()))

def I_Tarapacá(request):
  with open(d + "/Proyecto1/regiones/I - Tarapaca.html") as Documento_Ext:
    Plantilla = Template(Documento_Ext.read())
  Documento_Ext.close()
  return HttpResponse(Plantilla.render(Context()))

def II_Antofagasta(request):
  with open(d + "/Proyecto1/regiones/II - Antofagasta.html") as Documento_Ext:
    Plantilla = Template(Documento_Ext.read())
  Documento_Ext.close()
  return HttpResponse(Plantilla.render(Context()))

def III_Atacama(request):
  with open(d + "/Proyecto1/regiones/III - Atacama.html") as Documento_Ext:
    Plantilla = Template(Documento_Ext.read())
  Documento_Ext.close()
  return HttpResponse(Plantilla.render(Context()))

def IV_Coquimbo(request):
  with open(d + "/Proyecto1/regiones/IV - Coquimbo.html") as Documento_Ext:
    Plantilla = Template(Documento_Ext.read())
  Documento_Ext.close()
  return HttpResponse(Plantilla.render(Context()))

def V_Valparaiso(request):
  with open(d + "/Proyecto1/regiones/V - Valparaiso.html") as Documento_Ext:
    Plantilla = Template(Documento_Ext.read())
  Documento_Ext.close()
  return HttpResponse(Plantilla.render(Context()))

def RM_Metropolitana(request):
  with open(d + "/Proyecto1/regiones/RM - Metropolitana.html") as Documento_Ext:
    Plantilla = Template(Documento_Ext.read())
  Documento_Ext.close()
  return HttpResponse(Plantilla.render(Context()))

def VI_OHiggins(request):
  with open(d + "/Proyecto1/regiones/VI - OHiggins.html") as Documento_Ext:
    Plantilla = Template(Documento_Ext.read())
  Documento_Ext.close()
  return HttpResponse(Plantilla.render(Context()))

def VII_Maule(request):
  with open(d + "/Proyecto1/regiones/VII - Maule.html") as Documento_Ext:
    Plantilla = Template(Documento_Ext.read())
  Documento_Ext.close()
  return HttpResponse(Plantilla.render(Context()))

def XVI_Nuble(request):
  with open(d + "/Proyecto1/regiones/XVI - Nuble.html") as Documento_Ext:
    Plantilla = Template(Documento_Ext.read())
  Documento_Ext.close()
  return HttpResponse(Plantilla.render(Context()))

def VIII_Biobio(request):
  with open(d + "/Proyecto1/regiones/VIII - Biobio.html") as Documento_Ext:
    Plantilla = Template(Documento_Ext.read())
  Documento_Ext.close()
  return HttpResponse(Plantilla.render(Context()))

def IX_Araucania(request):
  with open(d + "/Proyecto1/regiones/IX - Araucania.html") as Documento_Ext:
    Plantilla = Template(Documento_Ext.read())
  Documento_Ext.close()
  return HttpResponse(Plantilla.render(Context()))

def XIV_LosRios(request):
  with open(d + "/Proyecto1/regiones/XIV - LosRios.html") as Documento_Ext:
    Plantilla = Template(Documento_Ext.read())
  Documento_Ext.close()
  return HttpResponse(Plantilla.render(Context()))

def X_LosLagos(request):
  with open(d + "/Proyecto1/regiones/X - LosLagos.html") as Documento_Ext:
    Plantilla = Template(Documento_Ext.read())
  Documento_Ext.close()
  return HttpResponse(Plantilla.render(Context()))

def XI_Aysen(request):
  with open(d + "/Proyecto1/regiones/XI - Aysen.html") as Documento_Ext:
    Plantilla = Template(Documento_Ext.read())
  Documento_Ext.close()
  return HttpResponse(Plantilla.render(Context()))

def XII_Magallanes(request):
  with open(d + "/Proyecto1/regiones/XII - Magallanes.html") as Documento_Ext:
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
