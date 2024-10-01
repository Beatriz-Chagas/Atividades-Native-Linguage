# Regressão Logística para identificar a probabilidade de chover com base em informações de cidades australianas


Com base no arquivo de informações de cidades australianas extraído do Dataset no Kaggle: https://www.kaggle.com/code/prashant111/logistic-regression-classifier-tutorial/input?select=weatherAUS.csv

Crie um modelo de Regressão Logística usando a biblioteca Scikit Learn para prever a probabilidade de chover com base nas variáveis independentes Temperatura Mínima e Temperatura Máxima existentes no arquivo

Utilize o campo Rainnfall como saída (variável dependente) para identificar se houve chuva, sendo que valor 0 indica que não chuva, e valores superiores a 0 indicam que houve chuva.


Para isto crie as seguintes etapas:

1. Carregue o arquivo para leitura, e gere três listas uma para cada variável independente e uma lista para a variável dependente

2. Transforme as listas criadas anteriormente em arrays do numpy. Atenção os valores de saída não podem ser números float, precisam ser valores discretos, ou números inteiros.

3. Separe o conjunto de dados entre treinamento e teste na proporção de 30% teste e 70% treinamento, utilize o random_state para fixar a semente de geração de números aleatório, fazendo com que sempre o mesmo conjunto de testes seja extraído.

4. Crie o modelo de Regressão Logística usando o Scikit Learn

5. Treine o modelo criado com os dados de treinamento, lembre-se que as informações que o modelo espera devem estar no formato (número de elementos, número de features)

6. Verifique o Score do modelo utilizando os valores de teste

7. Gere alguns valores para fazer a predição

8. Escolha um dos features e plote no gráfico o feature escolhido no eixo X e o resultado previsto no eixo Y