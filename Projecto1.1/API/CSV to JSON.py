import csv, json
import os

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

def DataProduct7CSVtoJSON():
    # FUNCIONA CON ESTE TIPO DE ESTRUCTURAS {'Region': '2021-12-07', 'Arica y Parinacota': '691', 'Tarapacá': '1453', 'Antofagasta': '2037', 'Atacama': '407', 'Coquimbo': '942', 'Valparaíso': '1522', 'Metropolitana': '18323', 'O’Higgins': '935', 'Maule': '886', 'Ñuble': '1173', 'Biobío': '2938', 'Araucanía': '1596', 'Los Ríos': '740', 'Los Lagos': '2344', 'Aysén': '303', 'Magallanes': '247'}
    Archivo = "DP7.csv"
    data = {}
    arch = open(dCSV + Archivo, "r", encoding="utf-8")
    lectorCSV = csv.DictReader(arch)
    for fila in lectorCSV:
        for Elemento in fila:
            if Elemento != "Region":
                data[Diccionario_Regiones[Elemento]] = fila[Elemento]    
    Nombre = Archivo.split(".")
    arch2 = open(dJSON + Nombre[0] + ".json", "w")
    arch2.write(json.dumps(data, indent=4))
    return "Done!"
    
def DataProduct4CSVtoJSON():
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
    return "Done!"

def DataProduct5CSVtoJSON():
    # FUNCIONA CON ESTE TIPO DE ESTRUCTURAS {'Region': '2021-12-07', 'Arica y Parinacota': '691', 'Tarapacá': '1453', 'Antofagasta': '2037', 'Atacama': '407', 'Coquimbo': '942', 'Valparaíso': '1522', 'Metropolitana': '18323', 'O’Higgins': '935', 'Maule': '886', 'Ñuble': '1173', 'Biobío': '2938', 'Araucanía': '1596', 'Los Ríos': '740', 'Los Lagos': '2344', 'Aysén': '303', 'Magallanes': '247'}
    Archivo = "DP5.csv"
    data = {}
    arch = open(dCSV + Archivo, "r", encoding="utf-8")
    lectorCSV = csv.DictReader(arch)
    for fila in lectorCSV:
        for Elemento in fila:
            if Elemento == "Fecha":
                ano, mes, dia = fila[Elemento].split("-")
                plantilla = "{} de {}, {}"
                if dia[0] == "0":
                    dia = dia[1]
                fecha = plantilla.format(dia, meses[mes], ano)
                data[Elemento] = fecha
            else:
                Seleccionado = Elemento.lower()
                data[Seleccionado] = fila[Elemento]  
    Nombre = Archivo.split(".")
    arch2 = open(dJSON + Nombre[0] + ".json", "w")
    arch2.write(json.dumps(data, indent=4))
    return "Done!"

    
#DataProduct4CSVtoJSON()
#DataProduct7CSVtoJSON()
DataProduct5CSVtoJSON()