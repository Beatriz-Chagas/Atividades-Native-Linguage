import numpy as np

# Fornescendo os dados
altura = np.array([1.65, 1.75, 1.80, 1.70, 1.68, 1.72, 1.78, 1.60, 1.85, 1.73, 1.69, 1.75, 1.62, 1.80, 1.77, 1.68, 1.79, 1.81, 1.76, 1.74])
peso = np.array([65, 70, 75, 80, 60, 68, 72, 58, 90, 72, 65, 70, 55, 78, 79, 62, 85, 88, 70, 75])

# Calculando o BMI
bmi = peso / (altura ** 2)

# Definndo as categorias de BMI 
categories = ['Abaixo do peso', 'Peso normal', 'Sobrepeso', 'Obesidade']
bmi_intervals = [(0, 18.5), (18.5, 25), (25, 30), (30, float('inf'))]

# Contando as pessoas em cada categoria
counts = [0, 0, 0, 0]
for i in bmi:
    if i < 18.5:
        counts[0] += 1
    elif 18.5 <= i < 25:
        counts[1] += 1
    elif 25 <= i < 30:
        counts[2] += 1
    else:
        counts[3] += 1

# Mostrando os resultados
print('BMI Categories:')
for i, category in enumerate(categories):
    print(f'{category}: {counts[i]} pessoas')