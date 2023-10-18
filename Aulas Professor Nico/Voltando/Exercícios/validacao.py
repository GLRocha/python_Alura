# Lista de nomes
nomes = ["Alice", "Bob", "Ana", "Arthur", "Eva"]

# Criar uma nova lista com nomes que começam com 'a'
nomes_com_a = [nome for nome in nomes if nome[0].lower() == 'a']

# Exibir a nova lista
print(nomes_com_a)

# Saída: ['Alice', 'Ana', 'Arthur']
