from datetime import datetime, timedelta
from requests import get

def getLastCovidData():
    substracting_days = 0
    while True:
        current_date = datetime.today()
        current_date = current_date - timedelta(days=substracting_days)
        today_date = current_date.strftime('%Y-%m-%d')
        url = f"https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto4/{today_date}-CasosConfirmados-totalRegional.csv"
        req = get(url)

        if "Not found" not in req.text:
            break

        substracting_days += 1

    return req.text

print(getLastCovidData())