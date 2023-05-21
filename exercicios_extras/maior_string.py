# Cria uma lista vazia
lista_strings = []

# Obtém as entradas do usuário
num_strings = int(input("Quantas strings você deseja inserir? "))

for i in range(num_strings):
    string = input("Digite uma string: ")
    lista_strings.append(string)

# Encontra a maior string
maior_string = max(lista_strings, key=len)

# Exibe a maior string
print("A maior string é:", maior_string)

