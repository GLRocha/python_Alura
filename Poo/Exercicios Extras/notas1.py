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


resultado = cria_lista(3)
print(resultado)
resultado = sorted(resultado, key=lambda x: x["nota"], reverse=True)
print(resultado)
"""for i in resultado:
    print(i)
    print(i[0], i[1], i[2])
"""
cont = 1
# print(f'{cont} Lugar: {resultado[0]["nome"]}, Nota: {resultado[0]["nota"]}')
for i in resultado:
    # print(i)
    # print(i["nome"], i["nota"], i["status"])
    if cont > 2:
        break

    print(f'{cont} Lugar: {i["nome"]}, Nota: {i["nota"]}')
    print (cont)
    cont += 1




