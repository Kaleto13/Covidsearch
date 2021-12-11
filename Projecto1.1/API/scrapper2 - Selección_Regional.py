from requests import get
import os
from datetime import datetime, timedelta
from requests import get
import csv, json

Diccionario_Regiones= {
    "Arica y Parinacota":"XV",
    "Tarapacá": "I",
    "Antofagasta": "II",
    "Atacama":"III",
    "Coquimbo":"IV",
    "Valparaíso":"V",
    "Metropolitana": "RM",
    "O’Higgins":"VI",
    "Maule":"VII",
    "Ñuble": "XVI",
    "Biobío": "VIII",
    "Araucanía":"IX",
    "Los Ríos":"XIV",
    "Los Lagos":"X",
    "Aysén":"XI",
    "Magallanes":"XII"
}

meses = {
    "01":"enero",
    "02":"febrero",
    "03":"marzo",
    "04":"abril",
    "05":"mayo",
    "06":"junio",
    "07":"julio",
    "08":"agosto",
    "09":"septiembre",
    "10":"octubre",
    "11":"noviembre",
    "12":"diciembre"
}

d = "/".join(os.getcwd().split("\\"))
dCSV= d + "/Projecto1.1/API/csv/" 
dJSON = d + "/Projecto1.1/API/json/"

#DP7 Data Product 7 - Exámenes PCR por región (Actualizado 10/12/2021)
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
    for i in range(-7,0):
        arch2.write(Lista[i])

    arch.close()
    arch2.close()
    os.remove(d + "/Projecto1.1/API/csv/DP7raw.csv")

def DataProduct7CSVtoJSON():
    PCRPorRegion()
    # FUNCIONA CON ESTE TIPO DE ESTRUCTURAS {'Region': '2021-12-07', 'Arica y Parinacota': '691', 'Tarapacá': '1453', 'Antofagasta': '2037', 'Atacama': '407', 'Coquimbo': '942', 'Valparaíso': '1522', 'Metropolitana': '18323', 'O’Higgins': '935', 'Maule': '886', 'Ñuble': '1173', 'Biobío': '2938', 'Araucanía': '1596', 'Los Ríos': '740', 'Los Lagos': '2344', 'Aysén': '303', 'Magallanes': '247'}
    Archivo = "DP7.csv"
    data = {"Encabezado":["Fecha", "Dato"]}
    arch = open(dCSV + Archivo, "r", encoding="utf-8")
    lectorCSV = csv.DictReader(arch)
    
    current_date = datetime.today()
    today_date = current_date.strftime('%Y-%m-%d')
    print(today_date)
    
    Fecha_Dato = 0
    for fila in lectorCSV:
        for Elemento in fila:
            if Elemento == "Region": 
                Fecha_Dato = fila[Elemento][-5:]
                Mes, Dia = Fecha_Dato.split("-")
                Fecha_Dato = "/".join([Dia, Mes])
            else:
                Objeto = Diccionario_Regiones[Elemento]
                if Objeto not in data:
                    data[Objeto] = []
                data[Objeto].append([Fecha_Dato, int(fila[Elemento])])
            
            if Elemento == today_date:
                data[Diccionario_Regiones[Elemento]] = fila[Elemento]    
    #print(data)
    Nombre = Archivo.split(".")
    arch2 = open(dJSON + Nombre[0] + ".json", "w")
    arch2.write(json.dumps(data, indent=4))
    arch.close()
    os.remove(d + "/Projecto1.1/API/csv/DP7.csv")
    return "DP7 - Done!"












#DP4 Data Product 4 - Casos totales por región
def CasosTotalesPorRegion():
    substracting_days = 0
    Limite = 7
    Lista_Directorios = []
    while substracting_days < Limite:
        current_date = datetime.today()
        current_date = current_date - timedelta(days=substracting_days)
        today_date = current_date.strftime('%Y-%m-%d')
        url = f"https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto4/{today_date}-CasosConfirmados-totalRegional.csv"
        req = get(url)
        if "Not Found" not in req.text:
            substracting_days += 1
        content = req.content
        arch = open(d + "/Projecto1.1/API/csv/DP4" + today_date + ".csv","wb")
        Lista_Directorios.append(d + "/Projecto1.1/API/csv/DP4" + today_date + ".csv")
        arch.write(content)  
        arch.close()
    '''
    in Lista_Directorios:
        Archivo_Analisis = open(Archivo, "r")
        if Archivo
        
        
        else:

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

    arch.close()
    arch2.close()
    os.remove(d + "/Projecto1.1/API/csv/DP4raw.csv")
    '''

CasosTotalesPorRegion()

def DataProduct4CSVtoJSON():
    CasosTotalesPorRegion()
    Archivo = "DP4.csv"
    data = {}
    arch = open(dCSV + Archivo, "r", encoding="utf-8")
    lectorCSV = csv.DictReader(arch)
    
    Region_Data = ""
    for fila in lectorCSV:
        for Elemento in fila:
            if Elemento == "Region":
                data[Diccionario_Regiones[fila[Elemento]]] = []
                Region_Data = Diccionario_Regiones[fila[Elemento]]
            else:
                data[Region_Data].append(fila[Elemento])
    Nombre = Archivo.split(".")
    arch2 = open(dJSON + Nombre[0] + ".json", "w")
    arch2.write(json.dumps(data, indent=4))
    return "DP4 - Done!"

CasosTotalesPorRegion()


#DP5 Data Product 5 - Totales Nacionales Diarios (Actualizado 10/12/2021)

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
    Listilla = Lista[0].split(",")
    Recoleccion = ",".join([Listilla[0], Listilla[2], Listilla[4], Listilla[5], Listilla[7]]) + "\n"
    arch2.write(Recoleccion)
    
    Indices = range(-7,0)
    for Indice in Indices:
        Listilla = Lista[Indice]
        Listilla = Listilla.strip().split(",")
        # Fecha, Casos Totales, Fallecidos, Activos, Nuevos Totales
        Recoleccion = [Listilla[0], Listilla[2], Listilla[4], Listilla[5], Listilla[7]]
        for Indice in range(0,5):
            if Recoleccion[Indice][-2:] == ".0":
                Recoleccion[Indice] = Recoleccion[Indice][:-2]
        Escrito = ",".join(Recoleccion)
        arch2.write(Escrito + "\n")
    arch.close()
    arch2.close()
    os.remove(d + "/Projecto1.1/API/csv/DP5raw.csv")

def DataProduct5CSVtoJSON():
    current_date = datetime.today()
    today_date = current_date.strftime('%Y-%m-%d')
    NacionalDiario()
    # FUNCIONA CON ESTE TIPO DE ESTRUCTURAS {'Region': '2021-12-07', 'Arica y Parinacota': '691', 'Tarapacá': '1453', 'Antofagasta': '2037', 'Atacama': '407', 'Coquimbo': '942', 'Valparaíso': '1522', 'Metropolitana': '18323', 'O’Higgins': '935', 'Maule': '886', 'Ñuble': '1173', 'Biobío': '2938', 'Araucanía': '1596', 'Los Ríos': '740', 'Los Lagos': '2344', 'Aysén': '303', 'Magallanes': '247'}
    Archivo = "DP5.csv"
    data = {}
    arch = open(dCSV + Archivo, "r", encoding="utf-8")
    lectorCSV = csv.DictReader(arch)
    fecha_salida = ""
    Contador = 0
    lista_elementos = ["Casos totales", "Fallecidos", "Casos activos", "Casos nuevos totales"]
    for fila in lectorCSV:
        for Elemento in lista_elementos:
            if Elemento not in data:
                data[Elemento] = [["Fecha", Elemento]]
            Fecha_Dato = fila["Fecha"][-5:]
            Mes, Dia = Fecha_Dato.split("-")
            Fecha_Dato = "/".join([Dia, Mes])
            data[Elemento].append([Fecha_Dato,fila[Elemento]])
        
        Contador += 1
        if Contador == 7:
            ano, mes, dia = fila["Fecha"].split("-")
            plantilla = "{} de {}, {}"
            if dia[0] == "0":
                dia = dia[1]
            fecha = plantilla.format(dia, meses[mes], ano)
            fecha_salida = fecha
            data["Resumen"] = [fecha]
            for Elemento in lista_elementos:
                data["Resumen"].append(fila[Elemento])
    print(data)
    Nombre = Archivo.split(".")
    arch2 = open(dJSON + Nombre[0] + ".json", "w")
    arch2.write(json.dumps(data, indent=4))
    arch.close()
    arch2.close()
    os.remove(d + "/Projecto1.1/API/csv/DP5.csv")
    return "DP5 - Done!, fecha de actualización: " + fecha_salida

'''
#Presione Run para actualizar las estadisticas de la página selección regional.    
print(DataProduct4CSVtoJSON())
print(DataProduct7CSVtoJSON())
print(DataProduct5CSVtoJSON())
'''