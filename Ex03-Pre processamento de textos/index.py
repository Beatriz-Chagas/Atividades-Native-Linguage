import re

def analise_texto(coment):
    texto = texto.lower()
    texto = re.sub(r'[^\w\s]','',coment)
    palavra = texto.split()

    return palavra;

coment = input("Insira sua experiência com o nosso produto: \n")
print(analise_texto(coment))