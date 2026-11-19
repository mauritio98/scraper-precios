# Scraper de precios de libros

Pequeño proyecto de práctica en Python que hace *web scraping* de [Books to Scrape](https://books.toscrape.com), una web pensada para practicar esta técnica.

## Qué hace

El script [titulo.py](titulo.py):

1. Recorre las 50 páginas del catálogo.
2. Extrae el **título** y el **precio** de cada libro.
3. Muestra cada libro por pantalla y marca con `BARATO:` los que cuestan menos de 20 £.
4. Guarda todos los datos en un archivo `libros.csv` (columnas `titulo` y `precio`).

Entre cada petición espera 1 segundo para no saturar el servidor.

## Requisitos

- Python 3
- Las librerías `requests` y `beautifulsoup4`

```bash
pip install requests beautifulsoup4
```

## Uso

```bash
python titulo.py
```

Al terminar se crea `libros.csv` en la misma carpeta. El archivo usa codificación `utf-8-sig`, así que se abre bien en Excel con acentos y el símbolo `£`.

> `libros.csv` está en el `.gitignore`, por lo que no se sube al repositorio.

## Ejemplo de salida

```
200
All products | Books to Scrape - Sandbox
A Light in the Attic - £51.77
Tipping the Velvet - £53.74
Soumission - £50.10
Sharp Objects - £47.82
Sapiens: A Brief History of Humankind - £54.23
The Requiem Red - £22.65
...
BARATO: Starving Hearts (Triangular Trade Trilogy, #1) 13.99
...
```

En total se procesan 1000 libros, de los cuales 196 se marcan como `BARATO`. La ejecución tarda al menos 50 segundos por la pausa de 1 segundo entre peticiones.

## Librerías usadas

- `requests`: descarga las páginas.
- `beautifulsoup4`: analiza el HTML y localiza los datos.
- `csv` y `time`: de la biblioteca estándar, para guardar el archivo y hacer pausas.
