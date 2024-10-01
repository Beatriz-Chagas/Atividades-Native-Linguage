import numpy as np
import matplotlib.pyplot as plt

# Carrega dados do arquivo (supondo que seja um arquivo CSV)
data = np.genfromtxt('population.csv', delimiter=',')

# Extrai anos e população urbana
anos = data[:, 0]
populacao_urbana = data[:, 1]

# Converte listas para arrays do NumPy
anos = np.array(anos)
populacao_urbana = np.array(populacao_urbana)

# Define a função linear
def funcao_linear(x, w, b):
    return w * x + b

# Inicializa valores de w e b
w = 0.1
b = 0.5

# Calcula y_hat
y_hat = funcao_linear(anos, w, b)

# Plota os dados e a linha de regressão linear inicial
plt.scatter(anos, populacao_urbana, label='Dados')
plt.plot(anos, y_hat, label='Regressão Linear Inicial', color='red')
plt.legend()
plt.show()

# Define a função de custo
def custo(y, y_hat):
    m = len(y)
    return np.sum((y_hat - y) ** 2) / (2 * m)

# Calcula o custo inicial
custo_atual = custo(populacao_urbana, y_hat)
print(f'Custo Inicial: {custo_atual:.2f}')

# Define as funções de atualização para w e b
def novo_w(w, x, y, y_hat, learn_rate):
    return w - learn_rate * np.sum((y_hat - y) * x)

def novo_b(b, x, y, y_hat, learn_rate):
    return b - learn_rate * np.sum(y_hat - y)

# Define a taxa de aprendizado
learn_rate = 0.01

# Realiza 30 iterações do descida de gradiente
for i in range(30):
    # Calcula y_hat
    y_hat = funcao_linear(anos, w, b)
    
    # Calcula o custo
    custo_atual = custo(populacao_urbana, y_hat)
    print(f'Iteração {i+1}, Custo: {custo_atual:.2f}')
    
    # Atualiza w e b
    w = novo_w(w, anos, populacao_urbana, y_hat, learn_rate)
    b = novo_b(b, anos, populacao_urbana, y_hat, learn_rate)

# Plota a linha de regressão linear otimizada
y_hat = funcao_linear(anos, w, b)
plt.scatter(anos, populacao_urbana, label='Dados')
plt.plot(anos, y_hat, label='Regressão Linear Otimizada', color='green')
plt.legend()
plt.show()

print(f'w Otimizado: {w:.2f}, b: {b:.2f}')