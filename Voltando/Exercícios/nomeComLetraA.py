# Faça um programa que receba uma lista de palavras e retorne uma nova lista contendo apenas as palavras que começam com a letra 'a'.
lista = []

for i in range(1,5):
    nomes = input("Informe um nome: ")
    lista.append(nomes)


nomes_com_a = [nome for nome in lista if nome[0].lower() == 'a']
print(f"Estes são os nomes com letra A: {nomes_com_a}")


