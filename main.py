import pandas as pd

data = [1,2,3,4,5]
etiquetas = ['a', 'b', 'c', 'd','e']

serie = pd.Series(data, index=etiquetas)
print (serie)

datos = {'Nombre': ['Alice', 'Bob', 'Claire'],
         'Edad': [25,30,35],
         'Ciudad': ['A', 'B', 'C']}
df = pd.DataFrame(datos)
print (df)

data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002, 2003],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
frame = pd.DataFrame(data)
print (frame)

frame_reordenado =pd.DataFrame(frame, columns=['year', 'state', 'pop'])
print (frame_reordenado)

frame2 = pd.DataFrame(data, columns=['year', 'state', 'pop', 'debt'],
                       index=['one', 'two', 'three', 'four', 'five', 'six'])
print (frame2)
print (frame2.columns)
