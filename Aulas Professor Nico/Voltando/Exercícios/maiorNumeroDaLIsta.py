# Escreva um programa que receba uma lista de números e retorne o maior número da lista.
lista = []

for i in range(1,5):
    numeros = int(input("Informe um numero: "))
    lista.append(numeros)

maior_numero = max(lista)
print(f"O maior numero é: {maior_numero}")