import numpy as np
import matplotlib.pyplot as plt

# Carregue o arquivo para leitura, e gere uma lista com os anos e outra lista com a população urbana
anos = []
pop_urbana = []
with open("population.csv", "r") as arquivo:
    cabecalho = arquivo.readline().strip().split(",")  # Leia o cabeçalho
    indice_ano = cabecalho.index("Year")  # Encontre o índice da coluna "Year"
    indice_pop_urbana = cabecalho.index("Urban Population")  # Encontre o índice da coluna "Urban Population"
    for linha in arquivo:
        vet_linha = linha.strip().split(",")
        anos.append(int(vet_linha[indice_ano]))  # Year
        pop_urbana.append(float(vet_linha[indice_pop_urbana]))  # Urban Population

# Transforme as listas criadas anteriormente em arrays do numpy
anos = np.array(anos)
pop_urbana = np.array(pop_urbana)

# Declare a função linear com o nome funcao_linear que recebera como parâmetros os valores de (x), (w) e (b) retornando o resultado da expressão (w * x) + b
def funcao_linear(x, w, b):
    return w * x + b

# Escolha um valor para (w), outro para (b) e aplique estes valores juntamente com o (x) na função linear, coloque o resultado em uma variável chamada y_hat
w = 0.1
b = 10
y_hat = funcao_linear(anos, w, b)

# Plote as informações em um gráfico sendo pontos para os valores de x e y, e plote uma reta com cor diferente para o x e y_hat
plt.scatter(anos, pop_urbana, label="População Urbana")
plt.plot(anos, y_hat, label="Regressão Linear", color="red")
plt.xlabel("Anos")
plt.ylabel("População Urbana")
plt.legend()
plt.show()

# Crie uma função de custo que receba (y) e (y_hat) calcule a somatória de (y_hat - y)² retornando a soma / (2 * m)
def custo(y, y_hat):
    m = len(y)
    return np.sum((y_hat - y) ** 2) / (2 * m)

# Execute a função de custo para analisar o custo da função com o (w) e o (b) informados anteriormente
custo_atual = custo(pop_urbana, y_hat)
print(f"Custo atual: {custo_atual:.2f}")

# Crie a função chamada novo_w que receberá os valores de (w), (x), (y), y_hat e learn_rate a função deverá calcular o novo valor de w com base na derivada parcial de w
def novo_w(w, x, y, y_hat, learn_rate):
    return w - learn_rate * np.sum((y_hat - y) * x) / len(y)

# Crie a função chamada novo_b que receberá os valores de (b), (x), (y), y_hat e learn_rate a função deverá calcular o novo valor de b com base na derivada parcial de b
def novo_b(b, x, y, y_hat, learn_rate):
    return b - learn_rate * np.sum(y_hat - y) / len(y)

# Faça uma rotina que execute umas 30 vezes
learn_rate = 0.01
for i in range(30):
    y_hat = funcao_linear(anos, w, b)
    custo_atual = custo(pop_urbana, y_hat)
    w = novo_w(w, anos, pop_urbana, y_hat, learn_rate)
    b = novo_b(b, anos, pop_urbana, y_hat, learn_rate)
    print(f"Iteração {i+1}: W={w:.2f}, B={b:.2f}, Custo={custo_atual:.2f}")

# Plote as informações em um gráfico sendo pontos para os valores de x e y, e plote uma reta com cor diferente para o x e y_hat com o (w) e (b) otimizados
y_hat = funcao_linear(anos, w, b)
plt.scatter(anos, pop_urbana, label="População Urbana")
plt.plot(anos, y_hat, label="Regressão Linear Otimizada", color="green")
plt.xlabel("Anos")
plt.ylabel("População Urbana")
plt.legend()
plt.show()