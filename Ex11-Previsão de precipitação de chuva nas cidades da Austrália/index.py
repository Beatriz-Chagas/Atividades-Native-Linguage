import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt

# Carregue o arquivo para leitura
arquivo = open("weatherAUS.csv", "r")

# Gere três listas uma para cada variável independente e uma lista para a variável dependente
temp_min = []
temp_max = []
vai_chover = []

# Lê o arquivo e preenche as listas
linha = arquivo.readline()  # Descartar o cabeçalho
linha = arquivo.readline()  # Ler a primeira linha

linhas_ignoradas = 0
while linha != "":
    vet_linha = linha.split(",")
    try:
        temperatura_minima = float(vet_linha[2])
        temperatura_maxima = float(vet_linha[3])
        chuva_mm = float(vet_linha[4])
        temp_min.append(temperatura_minima)
        temp_max.append(temperatura_maxima)
        vai_chover.append(0 if chuva_mm <= 0 else 1)
    except ValueError as e:
        linhas_ignoradas += 1
    linha = arquivo.readline()
print(f"Foram ignoradas {linhas_ignoradas} linhas")

# Transforme as listas criadas anteriormente em arrays do numpy
features = np.array([temp_min, temp_max]).T
label = np.array(vai_chover)

# Separe o conjunto de dados entre treinamento e teste na proporção de 30% teste e 70% treinamento
features_train, features_teste, label_train, label_teste = train_test_split(features, label, test_size=0.3, random_state=50)

# Crie o modelo de Regressão Logística usando o Scikit Learn
model = LogisticRegression()

# Treine o modelo criado com os dados de treinamento
model.fit(features_train, label_train)

# Verifique o Score do modelo utilizando os valores de teste
print("Score do modelo:", model.score(features_teste, label_teste))

# Gere alguns valores para fazer a predição
t_min = float(input("Informe a temperatura minima de amanhã: "))
t_max = float(input("Informe a temperatura maxima de amanhã: "))
resultado = model.predict([[t_min, t_max]])
print("Há probabilidade de", model.predict_proba([[t_min, t_max]])[0][1]*100, "%")
if resultado[0] == 1:
    print("de chover amanhã")
else:
    print("de não chover amanhã")

# Escolha um dos features e plote no gráfico o feature escolhido no eixo X e o resultado previsto no eixo Y
plt.scatter(features[:, 0], model.predict(features))
plt.xlabel("Temperatura Mínima")
plt.ylabel("Probabilidade de Chover")
plt.show()