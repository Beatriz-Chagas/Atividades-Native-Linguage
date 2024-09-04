import re

texto = input('Insira sua mensagem: \n')

def desabrevia(texto):
    corrigido ={
        "vc": "você",
        "eh": "é",
        "mto": "muito",
        "mt": "muito",
        "flw": "falou",
        "vlw": "valeu",
        "msg": "mensagem",
        "tmj": "tamo junto",
        "blz": "beleza",
        "qnd": "quando",
        "td": "tudo",
        "qlqr": "qualquer",
        "tmj": "tamo junto",
        "obg": "obrigado",
        "tdv": "tá de boa",
        "sussa": "suave",
        "ah": "ah tá",
        "kkk": "risada",
        "rs": "risada",
        "dp": "depois",
        "vdd": "verdade",
        "kkj": "risada sarcástica",
        "pfv": "por favor",
        "ctz": "certeza",
        "xau": "tchau",
        "agora": "agora",
        "blz": "beleza",
        "pdp": "pode pá",
        "tbm": "também",
        "tb": "também",
        "pq": "porque",
        "n": "não",
        "s": "sim",
        "tlg": "tá ligado",
        "qto": "quanto",
        "bj": "beijo",
        "bjs": "beijos",
        "fds": "fim de semana",
        "ftw": "for the win",
        "gg": "good game",
        "f": "respeito",
        "eae": "e aí",
        "sdv": "sigo de volta",
        "bb": "bebê"
    }

    abreviacao = ["blz", "pdp", "tlg", "XD", ":)", ">:["]

    palavra = texto.split()
    palavra_desabreviada = [corrigido.get(palavra,palavra) for palavra in palavra]

    palavra_certa = [palavra for palavra in palavra_desabreviada if palavra not in abreviacao]

    desabreviado = " ".join(palavra_certa)

    return desabreviado

print (desabrevia(texto))

