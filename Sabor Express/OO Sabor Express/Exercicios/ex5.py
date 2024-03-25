class Livro:
    livros = []
    
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponivel = True
        Livro.livros.append()
        
    def __str__(self) -> str:
        return f'{self.autor} | {self.titulo} | {self.ano_publicacao}'
    
    def listar_livros(self):
        print(f'{'Autor'.ljust(20)} | {'Título'.ljust(20)} | {'Ano de Publicação'.ljust(20)} | {'Status000'}')
        for livro in Livro.livros:
            print(f'{livro.autor.ljust(20)} | {livro.titulo.ljust(20)} | {livro.ano_publicacao.ljust(20)} | {livro.disponivel}')
            
    @property
    def verificar_disponibilidade(self):  # Renomeando o método para evitar conflito com o atributo
        return '☒' if self.disponivel else '☐'
    
    