# Faça um programa que receba uma lista de números e retorne a soma de todos os elementos.
lista = []

for i in range (1,9):
    elemento = int(input("Insira um número: "))
    lista.append(elemento)

lista_ordenada = sorted(lista)
print(f"Ordenando a lista.... \n {lista_ordenada}")
print(f"A soma dos valores da lista é: {sum(lista_ordenada)}")