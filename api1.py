
import requests as r
import datetime as dt

url = "https://api.covid19api.com/dayone/country/brazil"
req = r.get(url)
dados = req.json()

dados_filtrados = []
for filtro in dados:
    dados_filtrados.append([filtro["Confirmed"], filtro["Deaths"],filtro["Recovered"], filtro["Active"], filtro["Date"]])

dados_filtrados.insert(0, ["confirmados", "obitos", "recuperados", "ativos","data"])

for i in range(1, len(dados_filtrados)):
    ano = int (dados_filtrados[i][4][:4])
    mes = int(dados_filtrados[i][4][5:7])
    dia = int(dados_filtrados[i][4][8:10])

    data = dt.date(ano, mes, dia)
    dados_filtrados[i][4] = dt.datetime.strftime(data, "%Y-%B-%d")





''' Mais sobre data'''

d = dt.date(2001, 9, 11)
tday = dt.date.today()
#print(tday, d)


# datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)

tdelta = dt.timedelta(hours=12)
#print(tday + tdelta)


bday = dt.date(2016, 9, 24)
till_bday = bday - tday
#print(till_bday.days)

dt_agora = dt.datetime.now()
#print(dt_agora.strftime('%B %d, %Y'))

dt_str = 'July 24, 2016'
dt = dt.datetime.strptime(dt_str, '%B %d, %Y')
#print(dt)

# strftime - Datetime para String
# strptime - String para Datetime
