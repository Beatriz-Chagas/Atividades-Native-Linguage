# Regressão linear com base na população urbana da Índia no decorrer dos anos

Com base no arquivo de População da Índia extraído do Dataset no Kaggle: https://www.kaggle.com/datasets/akhileshthite/indias-population-simple-linear-regression

Faça uma regressão linear utilizando o campo ano (Year) como sendo a variável independente e o campo população urbana (Urban Population) como sendo a variável dependente. Para isto crie as seguintes etapas:

1. Carregue o arquivo para leitura, e gere uma lista com os anos e outra lista com a população urbana

2. Transforme as listas criadas anteriormente em arrays do numpy

3. Declare a função linear com o nome funcao_linear que recebera como parâmetros os valores de (x), (w) e (b) retornando o resultado da expressão (w * x) + b

4. Escolha um valor para (w), outro para (b) e aplique estes valores juntamente com o (x) na função linear, coloque o resultado em uma variável chamada y_hat

5. Plote as informações em um gráfico sendo pontos para os valores de x e y, e plote uma reta com cor diferente para o x e y_hat

6. Crie uma função de custo que receba (y) e (y_hat) calcule a somatória de (y_hat - y)² retornando a soma / (2 * m)

7. Execute a função de custo para analisar o custo da função com o (w) e o (b) informados anteriormente

8. Crie a função chamada novo_w que receberá os valores de (w), (x), (y), y_hat e learn_rate a função deverá calcular o novo valor de w com base na derivada parcial de w

9. Crie a função chamada novo_b que receberá os valores de (b), (x), (y), y_hat e learn_rate a função deverá calcular o novo valor de b com base na derivada parcial de b

10. Faça uma rotina que execute umas 30 vezes

- o Calculo do y_hat

- o Custo atual

- o Novo valor de W

- o Novo valor de B

- o Mostre os valores de W, B e Custo atual na tela

11. Plote as informações em um gráfico sendo pontos para os valores de x e y, e plote uma reta com cor diferente para o x e y_hat com o (w) e (b) otimizados

Instruções de Submissão:
- 
Submeta apenas os arquivos com a extensão .py que foram desenvolvidos por você