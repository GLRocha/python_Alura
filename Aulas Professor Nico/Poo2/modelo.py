class Filme:
    def __init__(self, nome, ano, duracao):
        self.nome = nome
        self.ano = ano
        self.duracao = duracao

class Serie:
    def __init__(self, nome, ano, temporada):
        self.nome = nome
        self.ano = ano
        self.temporada = temporada


vingadores = Filme('Guerra Infinita', 2018, 120)
print(vingadores.nome)


atlanta = Serie('Atlanta', 2017, 7)
print(f'Nome: {atlanta.nome}, Ano: {atlanta.ano}, Temporadas: {atlanta.temporada}')