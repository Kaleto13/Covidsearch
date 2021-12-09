from requests import get
import os
from datetime import datetime, timedelta
from requests import get


d = "/".join(os.getcwd().split("\\"))

#DP7 Data Product 7 - Exámenes PCR por región
def PCRPorRegion():
    url = f"https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto7/PCR_T.csv"
    # ESTE ARCHIVO ES DE TIPO T
    req = get(url)
    req = req.content

    arch = open(d + "/Projecto1.1/API/csv/DP7raw.csv","wb")
    arch.write(req)  
    arch.close()

    arch = open(d + "/Projecto1.1/API/csv/DP7raw.csv","r", encoding="utf-8")
    arch2 = open(d + "/Projecto1.1/API/csv/DP7.csv","w", encoding="utf-8")
    
    Lista = list(arch)
    arch2.write(Lista[0])
    arch2.write(Lista[-1])
    return "Done!"

#DP4 Data Product 4 - Casos totales por región
def CasosTotalesPorRegion():
    substracting_days = 0
    while True:
        current_date = datetime.today()
        current_date = current_date - timedelta(days=substracting_days)
        today_date = current_date.strftime('%Y-%m-%d')
        url = f"https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto4/{today_date}-CasosConfirmados-totalRegional.csv"
        req = get(url)

        if "Not Found" not in req.text:
            break
        else: 
            substracting_days += 1

    req = req.content
    arch = open(d + "/Projecto1.1/API/csv/DP4raw.csv","wb")
    arch.write(req)  
    arch.close

    arch = open(d + "/Projecto1.1/API/csv/DP4raw.csv","r", encoding="utf-8")
    arch2 = open(d + "/Projecto1.1/API/csv/DP4.csv","w", encoding="utf-8")
    
    # Region	Casos totales acumulados	Fallecidos totales	Casos confirmados recuperados	Casos confirmados por antigeno	Casos con sospecha de reinfeccion	Casos probables acumulados	Casos activos probables	Casos nuevos totales	Casos nuevos con sintomas	Casos nuevos sin sintomas*	Casos nuevos reportados por laboratorio	Casos nuevos confirmados por antigeno	Casos activos confirmados
    Nuevo_Archivo = []
    for linea in arch:
        linea = linea.strip().split(",")
        Region, Totales, Nuevos, Activos = linea[0], linea[1], linea[8], linea[13]
        Nuevo_Archivo.append([Region, Totales, Nuevos, Activos])
    
    for Linea in Nuevo_Archivo:
        if Linea[0] != "Se desconoce región de origen" and Linea[0] != "Total":
            arch2.write(",".join(Linea) + "\n")

    return "Done!"

#DP5 Data Product 5 - Totales Nacionales Diarios

def NacionalDiario():
    url = f"https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto5/TotalesNacionales_T.csv"
    # ESTE ARCHIVO ES DE TIPO T
    req = get(url)
    req = req.content

    arch = open(d + "/Projecto1.1/API/csv/DP5raw.csv","wb")
    arch.write(req)  
    arch.close

    arch = open(d + "/Projecto1.1/API/csv/DP5raw.csv","r", encoding="utf-8")
    arch2 = open(d + "/Projecto1.1/API/csv/DP5.csv","w", encoding="utf-8")
    
    Lista = list(arch)
    Indices = [0, -2, -1]
    Fallecido_DiaAnterior = 0
    for Indice in Indices:
        Listilla = Lista[Indice]
        Listilla = Listilla.strip().split(",")
        Recoleccion = [Listilla[0], Listilla[2], Listilla[4], Listilla[5], Listilla[7]]
        for Indi2 in range(len(Recoleccion)):
            if " " in Recoleccion[Indi2 ]:
                Recoleccion[Indi2] = Recoleccion[Indi2].split(" ")
                Recoleccion[Indi2] = "".join(Recoleccion[Indi2])
        Escrito = ",".join(Recoleccion)
        if Indice == 0:
            Escrito += ",FallecidosNuevos" + "\n"
        elif Indice == -2:
            Escrito += ",0" + "\n"
            Fallecido_DiaAnterior = int(Listilla[4][:-2])
        elif Indice == -1:
            Escrito += "," + str(int(Listilla[4]) - Fallecido_DiaAnterior) + "\n"
        arch2.write(Escrito)
        
    return "Done!"

# 16 Regiones
PCRPorRegion()
CasosTotalesPorRegion()
NacionalDiario()