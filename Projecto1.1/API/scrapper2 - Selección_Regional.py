from requests import get
import os

d = "/".join(os.getcwd().split("\\"))

#DP7 Data Product 7 - Exámenes PCR por región
def PCRPorRegion():
    url = f"https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto7/PCR_T.csv"
    # ESTE ARCHIVO ES DE TIPO T
    req = get(url)
    req = req.content

    arch = open(d + "/Projecto1.1/API/csv/DP7raw.csv","wb")
    arch.write(req)  
    arch.close

    arch = open(d + "/Projecto1.1/API/csv/DP7raw.csv","r", encoding="utf-8")
    arch2 = open(d + "/Projecto1.1/API/csv/DP7.csv","w", encoding="utf-8")
    
    Lista = list(arch)
    arch2.write(Lista[0])
    arch2.write(Lista[-1])
    return "Done!"
    
# 16 Regiones

PCRPorRegion()