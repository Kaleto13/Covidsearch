import os

d = "/".join(os.getcwd().split("\\"))
dCSV= d + "/Projecto1.1/API/csv/" 
dJSON = d + "/Projecto1.1/API/json/"

print(d)
arch = open(d + "/Proyecto1.1/Projecto1/static/js/graficos_seleccionRegional.js")

for linea in arch:
    print(linea)