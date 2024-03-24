class Restaurante:
    nome = ''
    categoria = ''
    ativo = False
    
restaurante_praca = Restaurante()
restaurante_praca.nome = 'Praca'
restaurante_praca.categoria = 'Italiana'
restaurante_praca.ativo = True
print((restaurante_praca.nome))
restaurante_pizza = Restaurante()
if restaurante_praca.ativo is False:
    print('Esse restaurante nao esta ativo')
else:
    print('O restaurante esta ativo')

bistro = Restaurante()
bistro.nome = 'Bistro'
print(bistro.nome)

categoria = Restaurante.categoria

restaurante_pizza = Restaurante()
restaurante_pizza.nome = 'Pizza Palace'
restaurante_pizza.categoria = 'Fast Food'
print((restaurante_pizza.categoria))
restaurante_pizza.ativo = True

if restaurante_pizza.categoria == 'Fast Food':
    print('A categoria é Fast Food.')
else:
    print('A categoria não é Fast Food.')


print(f'Nome: {restaurante_praca.nome}, Categoria: {restaurante_praca.categoria}')


