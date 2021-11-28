from django.http import HttpResponse
from django.template import Template, Context
import os

d = "/".join(os.getcwd().split("\\"))

def saludo(request):
  with open(d + "/Proyecto1/plantilas/saludo.html") as Documento_Ext:
    Plantilla = Template(Documento_Ext.read())
  Documento_Ext.close()
  return HttpResponse(Plantilla.render(Context()))

def estadisticas(request):
  with open(d + "/Proyecto1/plantilas/estadisticas.html") as Documento_Ext:
    Plantilla = Template(Documento_Ext.read())
  Documento_Ext.close()
  return HttpResponse(Plantilla.render(Context()))