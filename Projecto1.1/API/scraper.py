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

    #dicccc
    ret = {}
    for l in j:
        if len(l) == 2:
            ret[str(l[0])] = l[1]
        else:
            ret[str(l[0])] = ''
    return ret


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

#DP13 PCD acumulado e informado en el ultimo dia


def PCRAcumulado():
    substracting_days = 0
    while True:
        current_date = datetime.today()
        current_date = current_date - timedelta(days=substracting_days)
        today_date = current_date.strftime('%Y-%m-%d')
        url = f"https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto17/PCREstablecimiento.csv"
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
        j += str(raw[i][0])+','+str(raw[i][1])+','+str(raw[i][x-1])+';'
    j = j.strip().split(';')
    for i in range(len(j)):
        j[i] = j[i].split(',')
    
    dac = {}
    lac = []
    for l in range(len(j[0])):
        dac[j[0][l]] = []
        lac.append(j[0][l])
    
    for t in range(len(j)):
        if t == 0:
            pass
        else:
            for f in range(len(j[t])):
                dac[lac[f]].append(j[t][f])
    arch = open('DP17-PCREstablecimiento.csv', 'w')
    for f in dac:
        arch.write(f+',')
        for x in dac[f]:
            arch.write(x+',')
        arch.write('\n')
    arch.close()
    return True


def CasosNuevosCumulativo():
    substracting_days = 0
    while True:
        current_date = datetime.today()
        current_date = current_date - timedelta(days=substracting_days)
        today_date = current_date.strftime('%Y-%m-%d')
        url = f"https://github.com/MinCiencia/Datos-COVID19/blob/master/output/producto13/CasosNuevosCumulativo.csv"
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
        j += str(raw[i][0]) + ',' + str(raw[i][1]) + ',' + str(raw[i][2]) + ',' + \
            str(raw[i][3]) + ',' + str(raw[i][4]) + \
            ',' + str(raw[i][x-1]) + '\n'

    return j

#print(CasosTotalesPorRegion(), '\n')
#print(TotalNacionalesDiarios(), '\n') 
#print(PCRPorRegion(), '\n')
#print(PasoAPaso(), '\n')
#print(PCRAcumulado(), '\n')
print(CasosNuevosCumulativo(), '\n')
