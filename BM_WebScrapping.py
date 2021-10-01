# Primero importamos las librerías Python que utilizaremos:

import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime
import pandas as pd

# Indicamos la ruta de la web que deseamos acceder:
url_page = 'https://www.bolsamadrid.es/esp/aspx/Mercados/Precios.aspx?indice=ESI100000000'

# haremos el request a esa ruta y procesaremos el HTML mediante un objeto de tipo BeautifulSoap
page = requests.get(url_page).text 
soup = BeautifulSoup(page, "lxml")

# En nuestro caso nos interesa primero acceder a la tabla, y de allí a sus celdas. Por suerte la tabla tiene un id único
tabla = soup.find('table', attrs={'id': 'ctl00_Contenido_tblAcciones'})
tabla

# en este caso no tenemos un acceso directo a las celdas por ids únicos ni por clases, sólo nos queda iterar
name=""
price=""
var = ""
maxima = ""
minima = ""
nroFila=0
for fila in tabla.find_all("tr"):
    nroCelda=0
    for celda in fila.find_all('td'):
        if nroCelda==0:
            name=celda.text
            print("Accion:", name)
        if nroCelda==1:
            price=celda.text
            print("Valor:", price)
        if nroCelda==2:
            var=celda.text
            print("Variacion:", var)
        if nroCelda==3:
            maxima=celda.text
            print("Maxima:", maxima)
        if nroCelda==4:
            minima=celda.text
            print("Minima:", minima)
        nroCelda=nroCelda+1
    nroFila=nroFila+1

# Ya sólo nos queda guardar los datos para usar en el futuro.
    with open('acciones_bma.csv', 'a') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([name, price , var , maxima , minima ,datetime.now()])
        
# Pasamos el csv a un dataframe de Pandas
df = pd.read_csv('acciones_bma.csv')
df.columns = ["Nombre", "Precio", "Var.", "Max.", "Min.", "Fecha"]
df.to_csv('acciones_bma.csv')

# Mostramos las diez primeras lineas
df.head(10)

