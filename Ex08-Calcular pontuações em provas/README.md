# Cálculo de pontuações em provas

O professor da disciplina de Processamento de Linguagem Natural, aplicou uma avaliação no semestre para os alunos da turma, a avaliação foi dividida em várias seções, sendo que cada seção possui pesos diferentes.

Exercício: Faça um programa que utilize a biblioteca Numpy e calcule as pontuações da avaliação dos alunos de maneira automática.

· O programa deve pedir ao professor para que informe quantos alunos serão avaliados

· Depois deverá pedir a quantidade de seções existentes na avaliação

· Deverá em seguida pedir ao usuário para que informe os pesos das avaliações. Em seguida coloque-os em um array Numpy.

o Dica: Uma forma fácil de fazer consiste em criar uma lista e colocar os pesos nesta lista, e depois transformar a lista em um array Numpy. Após a conversão, faça um teste para verificar se a soma dos pesos é igual a 10,0

· Agora solicite para que o usuário digite as notas obtidas nas seções da avaliação, para cada aluno. Em seguida crie um array Numpy de duas dimensões sendo que a primeira dimensão serão os alunos e a segunda dimensão as notas obtidas nas seções da avaliação para cada aluno.

o Ex.:

[10, 8, 7], # Aluno 1

[9, 6, 5], # Aluno 2

[8, 7, 6], # Aluno 3

[7, 6, 8], # Aluno 4

[6, 5, 9] # Aluno 5

· Crie uma função que receba a matriz de respostas dos alunos e o vetor de pesos como entrada e retorne um vetor com as pontuações finais de cada aluno. Utilize o Numpy para fazer esta multiplicação

Instruções de Submissão:
- 
Submeta apenas os arquivos com a extensão .py que foram desenvolvidos por você