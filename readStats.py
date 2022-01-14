import pandas as pd
import requests

url = "https://datausa.io/api/data?measure=Household%20Income%20by%20Race,Household%20Income%20by%20Race%20Moe&Geography=16000US1304000:parents,16000US1304000,16000US1304000:similar"
ur = r"http://datausa.io/api/data"
urlPop = r"https://datausa.io/api/data?drilldowns=State&measures=Population"

r = requests.get(urlPop)
print(r.status_code)
print(r.text)
text = eval(r.text)
print(type(text))
