class Livro:
    livros = []
    
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponivel = True
        Livro.livros.append(self)
        
    def __str__(self) -> str:
        return f'{self.autor} | {self.titulo} | {self.ano_publicacao}'
    
    @classmethod
    def listar_livros(cls):
        print(f'{"Autor".ljust(20)} | {"Título".ljust(20)} | {"Ano de Publicação".ljust(20)} | {"Status".ljust(20)}')
        for livro in cls.livros:
            print(f'{livro.autor.ljust(20)} | {livro.titulo.ljust(20)} | {str(livro.ano_publicacao).ljust(20)} | {livro.verificar_disponibilidade()}')
    
    def verificar_disponibilidade(self): 
        return '☒' if self.disponivel else '☐'
    
    def emprestar(self):
        self.disponivel = False
    
    @staticmethod
    def verificar_disponibilidade(ano):
        livros_disponiveis = []
        for livro in Livro.livros:
            if livro.ano_publicacao == ano and livro.disponivel:
                livros_disponiveis.append(livro)
        return livros_disponiveis


# Criando algumas instâncias da classe Livro
livro1 = Livro("Dom Casmurro", "Machado de Assis", 1899)
livro2 = Livro("Memórias Póstumas de Brás Cubas", "Machado de Assis", 1881)
livro3 = Livro("O Guarani", "José de Alencar", 1857)
livro4 = Livro("Iracema", "José de Alencar", 1865)

# Emprestando alguns livros para teste
livro1.emprestar()
livro3.emprestar()

# Verificando a disponibilidade de livros publicados em um determinado ano
livros_disponiveis = Livro.verificar_disponibilidade()


print(f"Lista de livros disponíveis publicados em {ano}:")
for livro in livros_disponiveis:
    print(livro)
