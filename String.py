# questão 01
nome = input("Digite seu primeiro nome: ")
sobrenome = input("Digite seu sobrenome: ")

nome_completo = nome + " " + sobrenome
print("Bem-vinda, " + nome_completo + "!")


# questão 02
frase = input("Digite a frase: ")

espacos = frase.count(" ")
print("Espaços em branco:", espacos)


# questão 03
nome = input("Digite seu nome: ")

for i in range(len(nome)):
    print(nome[:i + 1])


# questão 04
numero = input("Digite o número: ")

if len(numero) == 8:
    numero = "9" + numero
elif len(numero) == 9 and numero[0] != "9":
    numero = "9" + numero

print("Número completo:", numero[:5] + "-" + numero[5:])


# questão 05
frase = input("Digite uma frase: ")

indices = []
total = 0

for i in range(len(frase)):
    if frase[i].lower() in "aeiou":
        indices.append(str(i))
        total += 1

print("Índices das vogais:", ", ".join(indices))
print("Total:", total, "vogais")
