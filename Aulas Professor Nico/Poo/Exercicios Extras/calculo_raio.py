"""
Crie uma classe chamada "Círculo" que tenha um atributo "raio" e dois métodos:
um método para calcular a área do círculo e outro para calcular o perímetro do círculo.
"""


class Circulo:
    def __init__(self, raio):
        self.raio = raio
        self.pi = 3.14

    def calcula_area(self):
        area = self.pi * self.raio
        print(f'A area é: {area}')

    def calcula_perimetro(self):
        perimetro = (self.pi * 2) * self.raio
        print(f'O perimetro é: {perimetro}')
