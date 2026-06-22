numeros = []

quantidade = int(input("Digite a quantidade de números (mínimo 4): "))

for i in range(quantidade):
    numero = int(input(f"Digite o {i + 1}º número: "))
    numeros.append(numero)

print("Lista original:", numeros)
print("3 primeiros elementos:", numeros[:3])
print("2 últimos elementos:", numeros[-2:])
print("Lista invertida:", numeros[::-1])
print("Índices pares:", numeros[::2])
print("Índices ímpares:", numeros[1::2])

urls = ["www.google.com", "www.gmail.com", "www.github.com",
        "www.reddit.com", "www.yahoo.com"]

dominios = []

for url in urls:
    dominios.append(url[4:-4])

print("URLs:", urls)
print("Domínios:", dominios)

from random import randint

numeros = []

for i in range(10):
    numeros.append(randint(-100, 100))

print("Lista ordenada:", sorted(numeros))
print("Lista original:", numeros)
print("Índice do maior valor:", numeros.index(max(numeros)))
print("Índice do menor valor:", numeros.index(min(numeros)))
print("Soma:", sum(numeros))
print("Média:", sum(numeros) / len(numeros))

lista1 = []
lista2 = []
lista3 = []

qtd1 = int(input("Digite a quantidade de elementos da lista 1: "))

for i in range(qtd1):
    lista1.append(int(input()))

qtd2 = int(input("Digite a quantidade de elementos da lista 2: "))

for i in range(qtd2):
    lista2.append(int(input()))

menor = min(len(lista1), len(lista2))

for i in range(menor):
    lista3.append(lista1[i])
    lista3.append(lista2[i])

if len(lista1) > len(lista2):
    lista3 += lista1[menor:]
else:
    lista3 += lista2[menor:]

print("Lista intercalada:", lista3)

from random import randint

lista1 = []
lista2 = []

for i in range(20):
    lista1.append(randint(0, 50))
    lista2.append(randint(0, 50))

interseccao = []

for numero in lista1:
    if numero in lista2 and numero not in interseccao:
        interseccao.append(numero)

interseccao.sort()

print("Lista 1:", lista1)
print("Lista 2:", lista2)
print("Intersecção:", interseccao)

from random import randint

lista = []

for i in range(20):
    lista.append(randint(0, 100))

tamanho = int(input("Tamanho para divisão: "))

sublistas = []

for i in range(0, len(lista), tamanho):
    sublistas.append(lista[i:i + tamanho])

print("Lista original:", lista)
print("Sublistas:", sublistas)

n = int(input("Digite n: "))

matriz = []

for i in range(n):
    linha = []

    for j in range(n):
        linha.append(i)

    matriz.append(linha)

print("Resultado:")
for linha in matriz:
    print(linha)
