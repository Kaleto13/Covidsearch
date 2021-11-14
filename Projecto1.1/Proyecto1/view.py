from django import http
from django.http import HttpResponse
from django.template import Template, Context

def saludo(request):
  Documento_Ext = open("./plantilas/default.html")
  Plantilla = Template(Documento_Ext.read())
  Documento_Ext.close()
  return HttpResponse(Plantilla.render(Context()))

  
def default(request):
  Documento_Ext = open("./plantilas/saludo.html")
  Plantilla = Template(Documento_Ext.read())
  Documento_Ext.close()
  return HttpResponse(Plantilla.render(Context()))
