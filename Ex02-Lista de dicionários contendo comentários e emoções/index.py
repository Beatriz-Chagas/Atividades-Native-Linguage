
# 1)
u1 = {  "Autor": "Joao",
        "Comentario": "Estou tão feliz hoje!",
        "Sentimento": "Positivo" }

u2 = {  "Autor": "Maria",
        "Comentario": "Este filme é tão triste. ",
        "Sentimento": "Negativo" }

u3 = {  "Autor": "Carlos",
        "Comentario": "Que dia chuvoso entediante...",
        "Sentimento": "Positivo" }

u4 = {  "Autor": "Ana",
        "Comentario": "Adorei a nova música da banda! ",
        "Sentimento": "Negativo" }

u5 = {  "Autor": "Roberto",
        "Comentario": "Eureka, consegui resolver este problema",
        "Sentimento": "Positivo" }

list_dicio = [u1, u2, u3, u4, u5]

#2)
qnt_coment_positivos = 0
qnt_coment_negativos = 0

for x in list_dicio:
    if x['Sentimento'] == "Positivo":
        qnt_coment_positivos +=  1
    if x['Sentimento'] == "Negativo":
        qnt_coment_negativos +=  1

print ("A quantidade de comentários positivos contabilizada é: ", qnt_coment_positivos)
print ("A quantidade de comentários negativos contabilizada é: ", qnt_coment_negativos)

#3)
total_coment =  len(list_dicio)

proporcao_positivos = qnt_coment_positivos / total_coment
proporcao_negativos = qnt_coment_negativos / total_coment

print (f"A proporção de comentários positivos é: {proporcao_positivos:.2f}")
print (f"A proporção de comentários negativos é: {proporcao_negativos:.2f}")

#4)
print ("Comentários positivos:")
for x in list_dicio:
    if x['Sentimento'] == "Positivo":
        print(x['Comentario'])

#5)
for x in list_dicio:
    if x['Sentimento'] == "Negativo":
        x["sentimento_valor"] = 0
    else:
        x["sentimento_valor"] = 1

print(list_dicio)



