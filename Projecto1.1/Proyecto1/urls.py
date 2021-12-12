"""Proyecto1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Proyecto1.view import estadisticas_generales, regiones, XV_Arica, DataProduct7, DataProduct4, DataProduct5, I_Tarapacá, II_Antofagasta, III_Atacama, IV_Coquimbo, V_Valparaiso, RM_Metropolitana, VI_OHiggins, VII_Maule, XVI_Nuble, VIII_Biobio, IX_Araucania, XIV_LosRios, X_LosLagos, XI_Aysen, XII_Magallanes

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', regiones),
    path('Estadisticas/', estadisticas_generales),
    #Regiones
    path('Arica-y-Parinacota/', XV_Arica),
    path('Tarapaca/', I_Tarapacá),
    path('Antofagasta/', II_Antofagasta),
    path('Atacama/', III_Atacama),
    path('Coquimbo/', IV_Coquimbo),
    path('Valparaiso/', V_Valparaiso),
    path('Metropolitana/', RM_Metropolitana),
    path('OHiggins/', VI_OHiggins),
    path('Maule/', VII_Maule),
    path('Nuble/', XVI_Nuble),
    path('Biobio/', VIII_Biobio),
    path('La-Araucania/', IX_Araucania),
    path('Los-Rios/', XIV_LosRios),
    path('Los-Lagos/', X_LosLagos),
    path('Aysen/', XI_Aysen),
    path('Magallanes/', XII_Magallanes),
    #JSON
    path('DP4.json', DataProduct4),
    path('DP5.json', DataProduct5),
    path('DP7.json', DataProduct7)
    ] 