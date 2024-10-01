# Regressão Logística para identificar a probabilidade de ter um ataque cardíaco com base nas informações do paciente


Com base no arquivo de Informações de Pacientes extraído do Dataset no Kaggle: https://www.kaggle.com/code/fahadmehfoooz/heartattack-prediction-with-91-8-accuracy/input?select=heart.csv

Crie um modelo de Regressão Logística usando a biblioteca Scikit Learn para prever um ataque cardíaco com base nas 6 variáveis independentes existentes no arquivo:

0 - idade - Idade da pessoa
1 - sexo - Gênero da pessoa
2 - cp - Tipo de dor no peito
3 - trtbps - Pressão arterial em repouso (em mm Hg)
4 - chol - Colesterol em mg/dl obtido via sensor de IMC
5 - fbs - (glicose em jejum > 120 mg/dl) (1 = verdadeiro; 0 = falso)


Utilize o último campo índice 13 para ser a saída (variável dependente) que determina se o paciente teve o ataque do coração.


Para isto crie as seguintes etapas:

1. Carregue o arquivo para leitura, e gere varias listas uma para cada variável independente e uma lista para a variável dependente

2. Transforme as listas criadas anteriormente em arrays do numpy

3. Separar o conjunto de dados entre treinamento e teste na proporção de 20% teste e 80% treinamento, utilize o random_state para fixar a semente de geração de números aleatório, fazendo com que sempre o mesmo conjunto de testes seja extraído.

4. Crie o modelo de Regressão Logística usando o Scikit Learn

5. Treine o modelo criado com os dados de treinamento, lembre-se que as informações que o modelo espera devem estar no formato (número de elementos, número de features)

6. Verifique o Score do modelo utilizando os valores de teste

7. Gere alguns valores para fazer a predição

8. Escolha um dos features e plote no gráfico o feature escolhido no eixo X e o resultado previsto no eixo Y