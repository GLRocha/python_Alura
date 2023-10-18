# Escreva um programa que receba uma lista de nomes e retorne o nome mais longo.
lista = []

for i in range(1,6):
    nome = input("Insira os nomes desejados: ")
    lista.append(nome)

nome_maior = max(lista, key=len)
print(nome_maior)