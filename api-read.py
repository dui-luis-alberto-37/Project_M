#!bin/usr/python3
import requests

url = "https://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?table=exoplanets&format=json"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()  # O response.text para otros formatos
    print(data)
else:
    print("Error al obtener los datos:", response.status_code)

