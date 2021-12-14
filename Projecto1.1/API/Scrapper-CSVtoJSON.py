from requests import get
import os
from datetime import datetime, timedelta
from requests import get
import csv, json
import locale

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

Diccionario_Codigo_Region= {
    "15":"Arica y Parinacota",
    "01":"Tarapacá",
    "02":"Antofagasta",
    "03":"Atacama",
    "04":"Coquimbo",
    "05":"Valparaíso",
    "13":"Metropolitana",
    "06":"O’Higgins",
    "07":"Maule",
    "16":"Ñuble",
    "08":"Biobío",
    "09":"Araucanía",
    "14":"Los Ríos",
    "10":"Los Lagos",
    "11":"Aysén",
    "12":"Magallanes"
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


#DP1 Data Product 1 y 74 - Casos totales por comuna incremental y Paso en el sistema Paso a Paso (Actualizado 11/12/2021)
# OBRAS EN ESTA FUNCIÓN
def DataProduct1_74_19JSON():
    url = f"https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto1/Covid-19.csv"
    # ESTE ARCHIVO ES DE TIPO ESTANDAR
    req = get(url)
    req = req.content

    arch = open(d + "/Projecto1.1/API/csv/DP1raw.csv","wb")
    arch.write(req)  
    arch.close()

    arch = open(d + "/Projecto1.1/API/csv/DP1raw.csv","r", encoding="utf-8")
    arch2 = open(d + "/Projecto1.1/API/csv/DP1.csv","w", encoding="utf-8")
    
    for linea in arch:
        linea = linea.strip().split(",")
        Region, Codigo_Comuna, Comuna, Cifra = linea[0],linea[3], linea[2], linea[-2]
        arch2.write(",".join([Region, Codigo_Comuna, Comuna, Cifra]) + "\n")
    arch2.close()
    arch.close()
    os.remove(d + "/Projecto1.1/API/csv/DP1raw.csv")
    
    # Obtención de DP74
    
    url = f"https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto74/paso_a_paso.csv"
    req = get(url)
    req = req.content
    arch = open(d + "/Projecto1.1/API/csv/DP74raw.csv","wb")
    arch.write(req)  
    arch.close()
    
    arch = open(d + "/Projecto1.1/API/csv/DP74raw.csv","r", encoding="utf-8")
    arch2 = open(d + "/Projecto1.1/API/csv/DP74.csv","w", encoding="utf-8")
    for linea in arch:
        linea = linea.strip().split(",")
        Region, Codigo_Comuna, Comuna, Zona, Paso = linea[1], linea[2], linea[3], linea[4], linea[-1]
        arch2.write(",".join([Region, Codigo_Comuna, Comuna, Zona, Paso]) + "\n")
    arch2.close()
    arch.close()
    os.remove(d + "/Projecto1.1/API/csv/DP74raw.csv")
    
    # Obtención de DP19
    
    url = f"https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto19/CasosActivosPorComuna.csv"
    req = get(url)
    req = req.content
    arch = open(d + "/Projecto1.1/API/csv/DP19raw.csv","wb")
    arch.write(req)  
    arch.close()
    
    arch = open(d + "/Projecto1.1/API/csv/DP19raw.csv","r", encoding="utf-8")
    arch2 = open(d + "/Projecto1.1/API/csv/DP19.csv","w", encoding="utf-8")
    for linea in arch:
        linea = linea.strip().split(",")
        Codigo_Region, Codigo_Comuna, Comuna, Poblacion, Activos = linea[1], linea[3], linea[2], linea[4], linea[-1]
        arch2.write(",".join([Codigo_Region, Codigo_Comuna, Comuna, Poblacion, Activos]) + "\n")
    arch2.close()
    arch.close()
    os.remove(d + "/Projecto1.1/API/csv/DP19raw.csv")
    
    
    data = {"fechas":[]}
    arch = open(d + "/Projecto1.1/API/csv/DP1.csv","r", encoding="utf-8")
    for linea in arch:
        linea = linea.strip().split(",")
        Region, Codigo_Comuna, Comuna, Cifra = linea[0], linea[1], linea[2], linea[3]
        if Region != "Region":
            if "Desconocido" in Comuna:
                Comuna = "Desconocido"
                Codigo_Comuna = ""
            if Cifra[-2:] == ".0" and Cifra != "":
                Cifra = int(Cifra[:-2])
                Cifra = ",".join(format(Cifra, ",").split(","))
            if Codigo_Comuna != "":
                if Codigo_Comuna[0] == "0":
                    Codigo_Comuna = Codigo_Comuna[1:]
            if Diccionario_Regiones[Region] not in data:
                data[Diccionario_Regiones[Region]] = []
            data[Diccionario_Regiones[Region]].append([Comuna, Codigo_Comuna, Cifra])
        else:
            Cifra = Cifra.split("-")
            Cifra = "/".join([Cifra[2] , Cifra[1], Cifra[0]])
            data["fechas"].append(["DP1", Cifra])
    arch.close()
    os.remove(d + "/Projecto1.1/API/csv/DP1.csv")
    
    arch = open(d + "/Projecto1.1/API/csv/DP19.csv","r", encoding="utf-8")
    for linea in arch:
        linea = linea.strip().split(",")
        Codigo_Region, Codigo_Comuna, Comuna, Poblacion, Activos = linea[0], linea[1], linea[2], linea[3], linea[4]
        if Codigo_Region != "Codigo region" and Comuna != "Total":
            if "Desconocido" in Comuna:
                Comuna = "Desconocido"
                Codigo_Comuna = ""
            if Activos[-2:] == ".0" and Activos != "":
                Activos = int(Activos[:-2])
                Activos = ",".join(format(Activos, ",").split(","))
            if Poblacion[-2:] == ".0" and Poblacion != "":
                Poblacion = int(Poblacion[:-2])
                Poblacion = ",".join(format(Poblacion, ",").split(","))
            if Codigo_Comuna != "":
                if Codigo_Comuna[0] == "0":
                    Codigo_Comuna = Codigo_Comuna[1:]
            i = 0
            while i < len(data[Diccionario_Regiones[Diccionario_Codigo_Region[Codigo_Region]]]):
                Lista_Comuna = data[Diccionario_Regiones[Diccionario_Codigo_Region[Codigo_Region]]][i]
                if Lista_Comuna[1] == Codigo_Comuna:
                    Lista_Comuna.insert(2, Poblacion)
                    Elementos = [Activos, "", "", ""]
                    for Elemento in Elementos:
                        Lista_Comuna.append(Elemento)
                i += 1   
        elif Codigo_Region == "Codigo region":
            Activos = Activos.split("-")
            Activos = "/".join([Activos[2] , Activos[1], Activos[0]])
            data["fechas"].append(["DP19", Activos])
    arch.close()
    os.remove(d + "/Projecto1.1/API/csv/DP19.csv")
    
    arch = open(d + "/Projecto1.1/API/csv/DP74.csv","r", encoding="utf-8")
    for linea in arch:
        linea = linea.strip().split(",")
        Region, Codigo_Comuna, Comuna, Zona, Paso = linea[0], linea[1], linea[2], linea[3], linea[4]
        if Region != "region_residencia":
            if Region == "La Araucanía":
                Region = Region[3:]
            i = 0
            while i < len(data[Diccionario_Regiones[Region]]):
                Lista_Comuna = data[Diccionario_Regiones[Region]][i]
                if Lista_Comuna[1] == Codigo_Comuna:
                    if Zona == "Rural":
                        Lista_Comuna[5] = Paso
                    if Zona == "Urbana":
                        Lista_Comuna[6] = Paso
                    if Zona == "Total":
                        Lista_Comuna[7] = Paso
                i += 1
        else:
            Paso = Paso.split("-")
            Paso = "/".join([Paso[2] , Paso[1], Paso[0]])
            data["fechas"].append(["DP74", Paso])
    arch.close()
    os.remove(d + "/Projecto1.1/API/csv/DP74.csv")
    

    for region in data:
        for comuna in data[region]:
            if region != "fechas":
                del comuna[1]
    arch2 = open(dJSON + "DP1 - DP74.json", "w")
    arch2.write(json.dumps(data, indent=4))
    arch.close()
    arch2.close()
    return "DP1 - DP74 Done!"



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
    for i in range(-10,0):
        arch2.write(Lista[i])
    arch.close()
    arch2.close()
    os.remove(d + "/Projecto1.1/API/csv/DP7raw.csv")

def DataProduct7CSVtoJSON():
    PCRPorRegion()
    # FUNCIONA CON ESTE TIPO DE ESTRUCTURAS {'Region': '2021-12-07', 'Arica y Parinacota': '691', 'Tarapacá': '1453', 'Antofagasta': '2037', 'Atacama': '407', 'Coquimbo': '942', 'Valparaíso': '1522', 'Metropolitana': '18323', 'O’Higgins': '935', 'Maule': '886', 'Ñuble': '1173', 'Biobío': '2938', 'Araucanía': '1596', 'Los Ríos': '740', 'Los Lagos': '2344', 'Aysén': '303', 'Magallanes': '247'}
    Archivo = "DP7.csv"
    data = {"Total":[["Fecha", "PCR"]]}
    arch = open(dCSV + Archivo, "r", encoding="utf-8")
    lectorCSV = csv.DictReader(arch)
    current_date = datetime.today()
    today_date = current_date.strftime('%Y-%m-%d')
    
    Fecha_Dato = 0
    for fila in lectorCSV:
        Cantidad = 0
        for Elemento in fila:
            if Elemento == "Region": 
                Fecha_Dato = fila[Elemento][-5:]
                Mes, Dia = Fecha_Dato.split("-")
                Fecha_Dato = "/".join([Dia, Mes])
            else:
                Objeto = Diccionario_Regiones[Elemento]
                if Objeto not in data:
                    data[Objeto] = [["Fecha", "Testeos PCR"]]
                data[Objeto].append([Fecha_Dato, int(fila[Elemento])])
                Cantidad += int(fila[Elemento])
            
            if Elemento == today_date:
                data[Diccionario_Regiones[Elemento]] = fila[Elemento]    
        data["Total"].append([Fecha_Dato, Cantidad])
    #print(data)
    Nombre = Archivo.split(".")
    arch2 = open(dJSON + Nombre[0] + ".json", "w")
    arch2.write(json.dumps(data, indent=4))
    arch.close()
    os.remove(d + "/Projecto1.1/API/csv/DP7.csv")
    return "DP7 - Done!"

#DP4 Data Product 4 - Casos totales por región
def CasosTotalesPorRegionJSON():
    substracting_days = 0
    Limite = 10
    Lista_Directorio = []
    Fechas_Directorio = []
    while True and substracting_days < Limite:
        current_date = datetime.today()
        current_date = current_date - timedelta(days=substracting_days)
        today_date = current_date.strftime('%Y-%m-%d')
        url = f"https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto4/{today_date}-CasosConfirmados-totalRegional.csv"
        req = get(url)
        if "Not Found" in req.text:
            Limite += 1
            substracting_days += 1
        else: 
            substracting_days += 1
            content = req.content
            arch = open(d + "/Projecto1.1/API/csv/DP4" + today_date + ".csv","wb")
            arch.write(content)  
            arch.close()
            Lista_Directorio.append(d + "/Projecto1.1/API/csv/DP4" + today_date + ".csv")
            Fechas_Directorio.append(today_date)
    
    data = {}
    Indice_Fecha = 0
    for Archivo in Lista_Directorio:
        Archivo_Analisis = open(Archivo, "r", encoding="utf-8")
        Fecha = "/".join([Fechas_Directorio[Indice_Fecha][-5:].split("-")[1], Fechas_Directorio[Indice_Fecha][-5:].split("-")[0]])
        Bandera = True
        for Linea in Archivo_Analisis:
            Linea = Linea.strip().split(",")
            if Bandera:
                Bandera = False
            else:
                Region, Totales, Fallecidos, Nuevos, Activos = Linea[0], Linea[1] ,Linea[2], Linea[8], Linea[13]
                if Region != "Se desconoce región de origen" and Region != "Total":
                    if Diccionario_Regiones[Region] not in data:
                        data[Diccionario_Regiones[Region]] = {
                            "Totales":[], 
                            "Fallecidos":[],
                            "Nuevos":[], 
                            "Activos":[]}
                    data[Diccionario_Regiones[Region]]["Totales"].append([Fecha, int(Totales)])
                    data[Diccionario_Regiones[Region]]["Fallecidos"].append([Fecha, int(Fallecidos)])
                    data[Diccionario_Regiones[Region]]["Nuevos"].append([Fecha, int(Nuevos)])
                    data[Diccionario_Regiones[Region]]["Activos"].append([Fecha, int(Activos)])
        Archivo_Analisis.close()       
        os.remove(Archivo)
        Indice_Fecha += 1
    for Region in data:
        Lista_Categorias = [["Fecha","Casos Totales"], ["Fecha","Fallecidos"], ["Fecha","Casos Nuevos",], ["Fecha","Casos Activos"]]
        indice = 0
        for Categoria in data[Region]:
            data[Region][Categoria].reverse()
            data[Region][Categoria].insert(0,Lista_Categorias[indice])
            indice += 1
            
    arch2 = open(dJSON + "DP4.json", "w")
    arch2.write(json.dumps(data, indent=4))
    return "DP4 - Done!"

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
    
    Indices = range(-10,0)
    for Indice in Indices:
        Listilla = Lista[Indice]
        Listilla = Listilla.strip().split(",")
        # Fecha, Casos Totales, Casoso Recuperados, Fallecidos, Activos, Nuevos Totales
        Recoleccion = [Listilla[0], Listilla[2],Listilla[4], Listilla[5], Listilla[7]]
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
    lista_elementos = ["Contagios","Fallecidos", "Activos", "Totales"]
    Dicc_Significados = {"Contagios":"Casos totales","Fallecidos":"Fallecidos", "Activos":"Casos activos", "Totales":"Casos nuevos totales"}
    for fila in lectorCSV:
        for Elemento in lista_elementos:
            if Elemento not in data:
                data[Elemento] = [["Fecha", Elemento]]
            Fecha_Dato = fila["Fecha"][-5:]
            Mes, Dia = Fecha_Dato.split("-")
            Fecha_Dato = "/".join([Dia, Mes])
            data[Elemento].append([Fecha_Dato,int(fila[Dicc_Significados[Elemento]])])
        
        Contador += 1
        if Contador == 10:
            ano, mes, dia = fila["Fecha"].split("-")
            plantilla = "{} de {}, {}"
            if dia[0] == "0":
                dia = dia[1]
            fecha = plantilla.format(dia, meses[mes], ano)
            fecha_salida = fecha
            data["Resumen"] = [fecha]
            for Elemento in lista_elementos:
                data["Resumen"].append(fila[Dicc_Significados[Elemento]])
    Nombre = Archivo.split(".")
    arch2 = open(dJSON + Nombre[0] + ".json", "w")
    arch2.write(json.dumps(data, indent=4))
    arch.close()
    arch2.close()
    os.remove(d + "/Projecto1.1/API/csv/DP5.csv")
    return "DP5 - Done!, fecha de actualización: " + fecha_salida

#Presione Run para actualizar las estadisticas de la página selección regional. 
print(DataProduct1_74_19JSON())
print(CasosTotalesPorRegionJSON())
print(DataProduct7CSVtoJSON())
print(DataProduct5CSVtoJSON())
