import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt

arquivo = open("weatherAUS.csv", "r")


linha = arquivo.readline()    # Descartar o cabecalho
linha = arquivo.readline()    # Ler a primeira linha


temp_min = []
temp_max = []
vai_chover = []

linhas_ignoradas = 0
while linha != "":
    vet_linha = linha.split(",")
    try: 
        temperatura_minima = float(vet_linha[2])
        temperatura_maxima = float(vet_linha[3])
        chuva_mm = float(vet_linha[4])
        temp_min.append(temperatura_minima)
        temp_max.append(temperatura_maxima)
        vai_chover.append( 0 if chuva_mm <= 0 else 1)
    except ValueError as e:
        linhas_ignoradas += 1
    linha = arquivo.readline()
print(f"Foram ignoradas {linhas_ignoradas} linhas")

features = np.array([temp_min, temp_max])
features.shape


features_train, features_teste, label_train, label_teste = train_test_split( features.T, vai_chover, random_state = 50 )
print(f"Teste Features: {len(features_teste)}  Train Features: {len(features_train)}")
print(f"Teste VaiChover: {len(label_teste)}  Train VaiChover: {len(label_train)}")

model = LogisticRegression()

model.fit(features_train, label_train)

model.score(features_teste, label_teste)

print("Informe a temperatura minima de amanhã:")
t_min = float(input())
print("Informe a temperatura maxima de amanhã:")
t_max = float(input())
resultado = model.predict([[t_min, t_max]])
# print(resultado[0])
print("Há probabilidade de 73%") 
if resultado[0] == 1:
    print("de chover amanhã")
else:
    print("de não chover amanhã")