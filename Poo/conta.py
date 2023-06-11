class Conta:
    def __init__(self, numero, titular, saldo, limite):
        print(f"Constuindo Objeto...{self}")
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limte = limite

    def extrato(self):
        print(f"O saldo de R${self.saldo} do titular {self.titular}")

    def deposita(self, valor):
        self.saldo += valor

    def saca(self, valor):
        self.saldo -= valor
