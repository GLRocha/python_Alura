class Conta:
    def __init__(self, numero, titular, saldo, limite):
        print(f"Constuindo Objeto...{self}")
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limte = limite

    def extrato(self):
        print(f"O saldo de R${self.__saldo} do titular {self.__titular}")

    def deposita(self, valor):
        self.__saldo += valor

    def saca(self, valor):
        self.__saldo -= valor

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)
