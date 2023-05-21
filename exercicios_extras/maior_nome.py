
def maior_nome_da_lista():
    lista = []
    while len(lista) <= 4:
        entrada = input('Informe o nome que deseja: ')
        lista.append(entrada)
        print(lista)
        continue
    maior_nome = max(lista, key=len)
    print(f'O maior nome desta lista é o de: {maior_nome}')


if __name__ == "__main__":
    maior_nome_da_lista()
