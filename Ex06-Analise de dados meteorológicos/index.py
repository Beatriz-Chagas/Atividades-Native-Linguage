import numpy as np

dados_meteorologicos = np.array([25, 26, 27, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12])

# Temperatura média anual
temperatura_media_anual = np.mean(dados_meteorologicos)
print("Temperatura média anual:", temperatura_media_anual)

# Temperatura máxima registrada
temperatura_maxima = np.max(dados_meteorologicos)
print("Temperatura máxima registrada:", temperatura_maxima)

# Temperatura mínima registrada
temperatura_minima = np.min(dados_meteorologicos)
print("Temperatura mínima registrada:", temperatura_minima)

# Desvio padrão da temperatura
desvio_padrao = np.std(dados_meteorologicos)
print("Desvio padrão da temperatura:", desvio_padrao)