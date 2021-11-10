from django import http
from django.http import HttpResponse
from django.template import Template, Context

def saludo(request):
  Documento_Ext = open("C:/Users/Usuario/OneDrive - Universidad Técnica Federico Santa María/Documentos/GitHub/Covidsearch/Projecto1.1/Proyecto1/plantilas/default.html")
  Plantilla = Template(Documento_Ext.read())
  Documento_Ext.close()
  return HttpResponse(Plantilla.render(Context()))

  
def default(request):
  Documento_Ext = open("C:/Users/Usuario/OneDrive - Universidad Técnica Federico Santa María/Documentos/GitHub/Covidsearch/Projecto1.1/Proyecto1/plantilas/saludo.html")
  Plantilla = Template(Documento_Ext.read())
  Documento_Ext.close()
  return HttpResponse(Plantilla.render(Context()))
