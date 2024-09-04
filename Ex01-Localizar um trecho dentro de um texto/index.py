texto = """Python é uma linguagem de programação poderosa e versátil.
É amplamente utilizada em desenvolvimento web, ciência de dados, 
inteligência artificial e muito mais."""

pos_ponto = texto.find('.')
pos_virgula = texto.find(',')

if pos_ponto != -1 and pos_virgula != -1 and pos_ponto < pos_virgula:
    novo_texto = ""
    
    for i in range(pos_ponto + 1, pos_virgula):
        novo_texto += texto[i]
    
    novo_texto = novo_texto.strip()
    
    print("Trecho coletado:", novo_texto)
else:
    print("Não foi possível encontrar o ponto seguido de uma vírgula no texto.")
