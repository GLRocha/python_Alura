print("**********************************")
print ("Bem-Vindo ao jogo da Adivinhação!")
print("**********************************")

numero_secreto = 43
total_de_tentativas = 3

for rodada in range (1, total_de_tentativas + 1):
    print(f"Rodada {rodada}, de {total_de_tentativas} tentativas")
    chute = int(input("Digite um numero entre 1 e 100: "))
    print(f"Você digitou {chute}")

    acertou = numero_secreto == chute
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if acertou:
        print("Você acertou!")
    else:
        if maior:
            print("Você errou! O seu chute foi maior do que o número secreto.")
        elif menor:
            print("Você errou! O seu chute foi menor do que o número secreto.")

print("Fim do jogo!")