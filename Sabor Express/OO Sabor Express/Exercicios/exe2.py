class Musica:
    musicas = []

    def __init__(self, nome, artista, duracao):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao
        Musica.musicas.append(self)

    def __str__(self):
        return f'{self.nome} | {self.artista} | {self.duracao}'

  
    def listar_musicas():
        for musica in Musica.musicas:
            print(f'Artista: {musica.nome}, Musica: {musica.artista}, Duracao: {musica.duracao}')

musica1 = Musica('Modo Aviao', 'Tiee', 3.38)
musica2 = Musica('Paciencia', 'Ferrugem', 3.53)

Musica.listar_musicas()
