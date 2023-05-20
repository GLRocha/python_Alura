def numero_primo():
    numero = int(input("Informe um numero: "))
    contador = 0
    primo = 0
    while primo <= numero or contador < 2:
        primo = primo + 1
        x = numero % primo
        if x == 0:
            contador = contador + 1
    if contador <= 2:
        print("É um número primo!")
    else:
        print("Nao eh um numero primo!")


numero_primo()
