from datetime import datetime, timedelta
from requests import get
import os

d = "/".join(os.getcwd().split("\\"))

#DP7 PCR POR REGION
def PCRPorRegion():
    url = f"https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto12/bulk/producto7.csv"
    req = get(url)
    req = req.content

    arch = open(d + "/Projecto1.1/API/csv/DP7raw.csv","wb")
    arch.write(req)  
    arch.close
    
    arch = open(d + "/Projecto1.1/API/csv/DP7raw.csv","r")
    
    for linea in arch:
        print(linea)
print(PCRPorRegion())


Arica y Parinacota,252110,2021/12/07,691.0,15,274.08670818293604
TarapacÃ¡,382773,2021/12/07,1453.0,1,379.59835202587436
Antofagasta,691854,2021/12/07,2037.0,2,294.42628068927837
Atacama,314709,2021/12/07,407.0,3,129.3258216320474
Coquimbo,836096,2021/12/07,942.0,4,112.66648805878751
ValparaÃ­so,1960170,2021/12/07,1522.0,5,77.64632659412193
Metropolitana,8125072,2021/12/07,18323.0,13,225.5118477719336
Oâ€™Higgins,991063,2021/12/07,935.0,6,94.34314468404128
Maule,1131939,2021/12/07,886.0,7,78.27276911565022
Ã‘uble,511551,2021/12/07,1173.0,16,229.3026501756423
BiobÃ­o,1663696,2021/12/07,2938.0,8,176.59476250468836
AraucanÃ­a,1014343,2021/12/07,1596.0,9,157.3432261079339
Los RÃ­os,405835,2021/12/07,740.0,14,182.34011359296267
Los Lagos,891440,2021/12/07,2344.0,10,262.9453468545275
AysÃ©n,107297,2021/12/07,303.0,11,282.3937295544144
Magallanes,178362,2021/12/07,247.0,12,138.48241217299648