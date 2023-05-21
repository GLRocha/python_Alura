def cria_lista():
    lista = []
    while len(lista) <= 4:
        entrada = int(input("Informe os numeros que deseja: "))
        lista.append(entrada)
        print(lista)
        continue
    print(f'A soma de todos os itens da lista eh: {sum(lista)}"')


if __name__ == "__main__":
    cria_lista()
