from quickchart import QuickChart
import requests as r
import datetime as dt

url = "https://api.covid19api.com/dayone/country/brazil"
req = r.get(url)
dados = req.json()

dados_filtrados = {
    "confirmados": [],
    "obitos": [],
    "recuperados": [],
    "ativos":[],
    "data" : []
}


for filtro in dados:
    dados_filtrados["confirmados"].append(filtro["Confirmed"])
    dados_filtrados["obitos"].append(filtro["Deaths"])
    dados_filtrados["recuperados"].append(filtro["Recovered"])
    dados_filtrados["ativos"].append(filtro["Active"])

    #filtra a data
    ano = int (filtro["Date"][:4])
    mes = int (filtro["Date"][5:7])
    dia = int (filtro["Date"][8:10])
    data = dt.datetime.strftime(dt.date(ano, mes, dia), "%d/%m/%Y")
    dados_filtrados["data"].append(data)


obitos = dados_filtrados["data"][::10]
data = dados_filtrados["obitos"][::10]

chart = {
    "type": "bar",
    "data": {
        "labels": obitos,
        "datasets": [{
            "label": "Obitos",
            "data": data
        }]
    }
}

url ="https://quickchart.io/chart"

resp = r.get(f'{url}?c={str(chart)}')

with open ("grafico2.jpeg", "wb") as image:
    image.write(resp.content)

# mostrar imagem:
# from PIL import Image
# from IPython.display import display
# img_pil = Image("C:\Users\thaly\OneDrive\Área de Trabalho" )
# display(img_pil)

# fazer qr code
# from urllib.parse import quote
# text = quote (resp)
# link = "https://quickchart.io/qr"
# resp1 = r.get(f'{link}?text={text})}')
# save_image("qrcode.png", (resp1.content))

