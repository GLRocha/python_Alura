
def cria_lista(numero):

    lista = []


    for i in range(numero):
        nome = input("Entre com o nome do aluno: ")
        nota = float(input(f"Entre com a nota do {nome}: "))
        print(f"O aluno {nome}, tirou a nota {nota}")
        print(type(nota))
        if nota >= 7:
            print("Parabens voce passou")
            status = "Aprovado"
        elif nota < 7 and nota >= 3:
            print("Nos vemos na recuperacao")
            status = "Recuperacao"
        else:
            print("Nos vemos ano que vem")
            status = "Reprovado"
        #lista.append([nome, nota, status])
        lista.append({"nome": nome,
                      "nota": nota,
                      "status": status
                      })
    return lista


resultado = cria_lista(1)
print(resultado)
"""for i in resultado:
    print(i)
    print(i[0], i[1], i[2])
"""
for i in resultado:
    print(i)
    print(i["nome"], i["nota"], i["status"])
