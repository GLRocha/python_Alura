class Pessoa:
    def __init__(self, nome, idade, profissao):
        self._nome = nome.title()
        self._idade = int(idade)
        self._profissao = profissao
        
    def informacoes_pessoa(self):
        print(f'{self._nome}, {self._profissao} Idade atual: {self._idade}')
    
    def aumentar_idade(self):
        self._idade += 1
        
        
pessoa1 = Pessoa('joao', 25, 'Programador') 
pessoa1.aumentar_idade()
pessoa1.informacoes_pessoa()


