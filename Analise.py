import pandas as pd

#Base de dados
base = pd.read_excel("dados.xlsx")

lucro = base["Valor Final"].sum()
print(lucro)


lucro_loja = base[["ID Loja" , "Valor Final"]]
print(lucro_loja)