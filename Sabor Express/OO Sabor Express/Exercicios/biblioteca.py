from ex5 import Livro


# Criando algumas instâncias da classe Livro
livro1 = Livro("Dom Casmurro", "Machado de Assis", 1899)
livro2 = Livro("Memórias Póstumas de Brás Cubas", "Machado de Assis", 1881)
livro3 = Livro("O Guarani", "José de Alencar", 1857)
livro4 = Livro("Iracema", "José de Alencar", 1865)



livro2.emprestar()
livro2.verificar_disponibilidade(ano=1881)
livro2.emprestar()
livro2.verificar_disponibilidade()


def main ():
    Livro.listar_livros


if __name__ == '__main__':
    main()