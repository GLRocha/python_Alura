def polindrono():
    palavra = input("Digite uma palavra: ")
    print(f"Essa palavra tem {len(palavra)} letras")
    if palavra == "".join(reversed(palavra)):
        print("Essa palavra é um polindrono!")
    else:
        print("Essa palavra nao eh um polindrono!")


polindrono()
