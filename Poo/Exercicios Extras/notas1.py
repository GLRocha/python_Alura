def cria_lista(numero):
    lista = []

    nome = input("Entre com o nome do aluno: ")
    nota = float(input(f"Entre com a nota do {nome}: "))
    print(f"O aluno {nome}, tirou a nota {nota}")
    print(type(nota))

    if nota >= 7:
        print("Parabens, você passou")
        status = "Aprovado"
    elif nota < 7 and nota >= 3:
        print("Nos vemos na recuperacao")
        status = "Recuperacao"
    else:
        print("Nos vemos ano que vem")
        status = "Reprovado"

    lista.append({"nome": nome, "nota": nota, "status": status})
    lista = sorted(lista, key=lambda x: x["nota"], reverse=True)

    return lista


numero = 1
resultado = cria_lista(numero)
print(resultado)

for i in resultado:
    print(i)
    print(i["nome"], i["nota"], i["status"])
