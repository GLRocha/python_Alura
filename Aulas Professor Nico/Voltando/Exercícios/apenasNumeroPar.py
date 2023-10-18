# Crie um programa que receba uma lista de números e retorne uma nova lista apenas com os números pares.
lista = []

for i in range(1,9):
    entrada = int(input("Informe os números desejados: "))
    lista.append(entrada)


listaPares = []
for pares in lista:
    if pares % 2 == 0:
        listaPares.append(pares)


pares1 = sorted(listaPares)
print(f"Os números pares, são: {pares1}")