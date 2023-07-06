# Escreva um programa que remova todos os elementos duplicados de uma lista.

"""lista = [5, 8, 9, 15, 78, 96, 37, 48, 5, 78, 5, 48]
lista1 = []

for i in lista:
    if i not in lista1:
        lista1.append(i)

print(lista1)
"""
from typing import List

# Escreva um programa que inverta a ordem dos elementos em uma lista.
lista = [5, 8, 9]
lista1: list[int] = []

index_lista = len(lista) - 1

while index_lista >= 0:
    lista1.append(lista[index_lista])
    index_lista -= 1
print(lista1) 