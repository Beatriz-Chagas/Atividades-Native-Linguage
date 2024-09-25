import numpy as np

# Perguntar ao professor quantos alunos serão avaliados
num_alunos = int(input("Informe o número de alunos a serem avaliados: "))

# Perguntar a quantidade de seções existentes na avaliação
num_secoes = int(input("Informe o número de seções na avaliação: "))

# Perguntar os pesos das avaliações e criar um array Numpy
pesos = []
for i in range(num_secoes):
    peso = float(input(f"Informe o peso da seção {i+1}: "))
    pesos.append(peso)
pesos_array = np.array(pesos)

# Verificar se a soma dos pesos é igual a 10.0
if np.sum(pesos_array) != 10.0:
    print("Erro: A soma dos pesos deve ser igual a 10.0")
    exit()

# Solicitar as notas obtidas nas seções da avaliação para cada aluno
notas = []
for i in range(num_alunos):
    nota = input(f"Informe as notas do aluno {i+1} (separadas por espaço): ")
    notas.append([float(x) for x in nota.split()])
notas_array = np.array(notas)

# Criar uma função que calcula as pontuações finais de cada aluno
def calcular_pontuacoes(notas, pesos):
    return np.dot(notas, pesos)

# Calcular as pontuações finais de cada aluno
pontuacoes = calcular_pontuacoes(notas_array, pesos_array)

# Imprimir as pontuações finais de cada aluno
for i, pontuacao in enumerate(pontuacoes):
    print(f"Aluno {i+1}: Pontuação final = {pontuacao:.2f}")
