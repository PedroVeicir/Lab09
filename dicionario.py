#Questao 1

def contagem_caracteres(texto):
    contagem = {}

    for caractere in texto:
        if caractere in contagem:
            contagem[caractere] += 1
        else:
            contagem[caractere] = 1

    return contagem

texto = input("Diga uma frase ou palavra: ")
resultado = contagem_caracteres(texto)
print(resultado)

#Questao 3

def mesclar_dicionarios(dic1, dic2):
    resultado = dic1.copy()

    for chave, valor in dic2.items():
        if chave in resultado:
            if valor > resultado[chave]:
                resultado[chave] = valor
        else:
            resultado[chave] = valor

    return resultado


dicionario1 = eval(input("Digite o primeiro dicionário: "))
dicionario2 = eval(input("Digite o segundo dicionário: "))

resultado = mesclar_dicionarios(dicionario1, dicionario2)
print(resultado)

#Questao 4

def filtrar_dicionario(dicionario, lista_chaves):
    resultado = {}

    for chave in lista_chaves:
        if chave in dicionario:
            resultado[chave] = dicionario[chave]

    return resultado


dados = eval(input("Digite o dicionário: "))
chaves_filtradas = input("Digite as chaves separadas por espaço: ").split()

resultado = filtrar_dicionario(dados, chaves_filtradas)
print(resultado)

#Questao 5

def resultado_votacao(lista_votos):
    totais = {}

    for sessao in lista_votos:
        for candidato, votos in sessao.items():
            if candidato in totais:
                totais[candidato] += votos
            else:
                totais[candidato] = votos

    soma_total = sum(totais.values())

    resultado = {}

    for candidato, total in totais.items():
        percentual = round((total / soma_total) * 100, 2)
        resultado[candidato] = (total, percentual)

    return resultado


quantidade = int(input("Quantas sessões de votação? "))

votos = []

for i in range(quantidade):
    print(f"Sessão {i + 1}")
    sessao = eval(input("Digite o dicionário de votos: "))
    votos.append(sessao)

resultado = resultado_votacao(votos)
print(resultado)
