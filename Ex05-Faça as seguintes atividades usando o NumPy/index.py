# 1. Importe a biblioteca NumPy e crie um array NumPy de números inteiros de 1 a 10.
import numpy as np;
array1 = np.arange(1, 11)
print(array1)

# 2. Crie um array Numpy de números float aleatórios entre 0 e 1 nas seguintes dimensões 300 x 200 x 3
array2 = np.random.rand(300, 200, 3)
print(array2.shape)

# 3. Crie um array de duas dimensões para guardar notas de alunos de uma disciplina, sendo que existem 20 alunos na sala e cada aluno possuirá 3 notas na disciplina. O array deverá conter números aleatórios inteiros entre 1 e 10 (inclusive)
array3  = np.random.randint(1, 11, (20, 3))
print(array3)

# 4. Crie um array NumPy com 12 elementos e o redimensione em uma matriz 3x4. Em seguida, realize a transposição dessa matriz.
array4 = np.arange(1, 13)
array = array4.reshape(3, 4)
print("Original matrix:")
print(array)
print("Transposed matrix:")
print(array.T)

# 5. Crie dois arrays NumPy de mesma forma e realize as quatro operações aritméticas básicas (+, -, *, /) entre eles.
array51 = np.random.rand(2, 3)
array52 = np.random.rand(2, 3)
print('Array 1: ')
print(array51)
print('Array 2: ')
print(array52)
print("Adição:")
print(np.add(array51, array52))
print("Subtração:")   
print(np.subtract(array51, array52))
print("Multiplicação:")
print(np.multiply(array51, array52))
print("Divisão:")
print(np.divide(array51, array52))

# 6. Crie um array NumPy de números de 1 a 20 e, em seguida, imprima os elementos pares utilizando indexação e fatiamento.
array6 = np.arange(1,21)
print("Original array:")
print(array6)
print("Even elements:")
print(array6[1::2])

# 7. Crie um array NumPy de números aleatórios entre 1 e 100. Em seguida, selecione e exiba apenas os números maiores que 50.
array7 = np.random.randint(1, 101, 20)
print("Original array:")
print(array7)
print("Números maiores que 50:")

print(array7[array7 > 50])

# 8. Crie um array NumPy com 10 números aleatórios e calcule a média, mediana e desvio padrão desses números.
array8 = np.random.rand(10)
print("Original array:")
print(array8)
print("Média:", np.mean(array8))
print("Mediana:", np.median(array8))
print("Desvio padrão:", np.std(array8))
