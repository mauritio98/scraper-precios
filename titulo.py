import requests
from bs4 import BeautifulSoup
import csv

url = "https://books.toscrape.com"
respuesta = requests.get(url)
respuesta.encoding = "utf-8"
print(respuesta.status_code)

soup = BeautifulSoup(respuesta.text, "html.parser")
print(soup.title.string.strip())
libros = soup.find_all("article", class_="product_pod")

filas = []

for libro in libros:
    titulo = libro.h3.a["title"]
    precio = libro.find("p",class_="price_color").text
    print(titulo, "-", precio)
    precio_num = float(precio.replace("£", ""))
    filas.append([titulo, precio_num])
    if precio_num < 20:
        print("BARATO:", titulo, precio_num)

with open("libros.csv", "w", newline="", encoding="utf-8-sig") as archivo:
    escritor = csv.writer(archivo)
    escritor.writerow(["titulo", "precio"])
    escritor.writerows(filas)

    
