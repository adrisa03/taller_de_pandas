import pandas as pd

#cargar BD desde un archivo csv
data = pd.read_csv('anime.csv')
print(data.head()) #mostrar primeras 5 filas 
