from datetime import datetime, timedelta
from requests import get
import os

d = "/".join(os.getcwd().split("\\"))

#DP4 Ca
def PCRPorRegion():
    url = f"https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto7/PCR_T.csv"
    req = get(url)
    req = req.content

    arch = open(d + "/Projecto1.1/API/csv/DP7raw.csv","wb", encoding="utf-8")
    arch.write(req)  
    arch.close

    arch = open(d + "/Projecto1.1/API/csv/DP7raw.csv","r", encoding="utf-8")
    arch2 = open(d + "/Projecto1.1/API/csv/DP7.csv","r", encoding="utf-8")
    
    list = list(arch2)
    arch2.write(list[-16:])
    
# 16 Regiones