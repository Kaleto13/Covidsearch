from datetime import datetime, timedelta
from requests import get


#DP4 CASOS TOTALES POR REGION
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

    return req.text


#DP5 TOTAL NACIONALES DIARIOS
def TotalNacionalesDiarios():
    substracting_days = 0
    while True:
        current_date = datetime.today()
        current_date = current_date - timedelta(days=substracting_days)
        today_date = current_date.strftime('%Y-%m-%d')
        url = f"https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto5/TotalesNacionales.csv"
        req = get(url)

        if "Not Found" not in req.text:
            break
        else: 
            substracting_days += 1
    raw = req.text
    raw = raw.split('\n')

    for i in range(len(raw)):
        
        raw[i] = raw[i].split(',')

    j = ''
    for i in range(len(raw)-1):
        
        x = len(raw[i])
        j += str(raw[i][0]) + ',' + str(raw[i][x-1]) + ';'
    j = j.strip().split(';')
    for i in range(len(j)):
        j[i] = j[i].split(',')
    print(j)
    #dicccc
    ret = {}
    for l in j:
        if len(l) == 2:
            ret[str(l[0])] = [l[1]]
        else:
            ret[str(l[0])] = ''
    return ret


def TotalNacionalesDiarios2():
    substracting_days = 0
    while True:
        current_date = datetime.today()
        current_date = current_date - timedelta(days=substracting_days)
        today_date = current_date.strftime('%Y-%m-%d')
        url = f"https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto5/TotalesNacionales.csv"
        req = get(url)

        if "Not Found" not in req.text:
            break
        else:
            substracting_days += 1
    raw = req.text
    raw = raw.split('\n')

    for i in range(len(raw)):

        raw[i] = raw[i].split(',')
    j = ''
    for i in range(len(raw)-1):

        x = len(raw[i])
        j += str(raw[i][0]) + ',' + str(raw[i][x-1]) + ',' + str(raw[i][x-2]) + ',' + str(raw[i][x-3]) + ',' + str(raw[i][x-4]) + ',' + str(raw[i][x-5]) + ',' + str(raw[i][x-6]) + ',' + str(raw[i][x-7]) + ';'
    j = j.strip().split(';')
    for i in range(len(j)):
        j[i] = j[i].split(',')
    casos_activos = []
    casos_totales = []
    n_recuperados = []
    for l in range(len(j[0])):
        if l == 0:
            pass
        else:
            casos_activos.append([j[0][l], j[5][l]])
            casos_totales.append([j[0][l], j[2][l]])
            n_recuperados.append([j[0][l], j[10][l]])
    
    #arch = open(d + "/Projecto1.1/API/csv/ca")
    return(casos_activos)#, casos_totales, n_recuperados)
            

#DP7 PCR POR REGION     SE DEVUELVEN TODAS LAS FECHAS YA QUE LA INFORMACION DEL DIA ES BASTANTE INUTIL
def PCRPorRegion():
    url = f"https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto7/PCR.csv"
    req = get(url)

    '''if "Not Found" not in req.text:
        break
    else: 
        substracting_days += 1'''

    return req.text


#DP74 PASO A PASO POR REGION CON TODAS SUS COMUNAS.    FORMATO: CODIGO DE REGION | REGION | CODIGO COMUNA | COMUNA | ZONA | FASE POR FECHA (SOLO FECHA ACTUAL)
def PasoAPaso():
    substracting_days = 0
    while True:
        current_date = datetime.today()
        current_date = current_date - timedelta(days=substracting_days)
        today_date = current_date.strftime('%Y-%m-%d')
        url = f"https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto74/paso_a_paso.csv"
        req = get(url)

        if "Not Found" not in req.text:
            break
        else: 
            substracting_days += 1
    raw = req.text
    raw = raw.split('\n')

    for i in range(len(raw)):
        
        raw[i] = raw[i].split(',')

    j = ''

    for i in range(len(raw)-1):
        
        x = len(raw[i])
        j += str(raw[i][0]) + ',' + str(raw[i][1]) + ',' + str(raw[i][2]) + ',' + str(raw[i][3]) + ',' + str(raw[i][4]) + ',' + str(raw[i][x-1]) + '\n'

    return j



#print(CasosTotalesPorRegion(), '\n')
#print(TotalNacionalesDiarios(), '\n') 
print(TotalNacionalesDiarios2(), '\n')
#print(PCRPorRegion(), '\n')
#print(PasoAPaso(), '\n')
#print(PCRAcumulado(), '\n')
#print(CasosNuevosCumulativo(), '\n')
