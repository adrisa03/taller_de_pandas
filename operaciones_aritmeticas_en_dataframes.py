import pandas as pd

datos1 = {'A': [1, 2, 3], 'B': [4, 5, 6]}

df1 = pd.DataFrame(datos1)


#sunmar 10 a todas las entradas
df_suma = df1 + 10
print(df_suma)

serie = pd.Series([10, 20], index = ['A', 'B'])

#Sumar la serie al dataframe
resultado = df1 + serie
print(resultado)

datos2 = {'A': [10, 20, 30], 'B': [40, 50, 60]}
df2 = pd.DataFrame(datos2)

#Sumar ambos dataframes
df_suma2 = df1 + df2
print(df_suma2)

