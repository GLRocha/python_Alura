"""Crie uma classe chamada "Pessoa" que tenha os atributos "nome" e "idade".
Em seguida, crie um objeto dessa classe
e imprima os valores dos atributos.
"""


class Pessoas:
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade

    def retorna_dados(self):
        print(f'{self.__nome}, {self.__idade}')
