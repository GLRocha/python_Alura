from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

 
restaurante_praca = Restaurante('Praca', 'Gourmet')
bebida_suco = Bebida('Suco de Melancia', 5.00, 'Grande')
prato_torrada = Prato('Torrada', 3.50, 'Misto quente')


def main():
   print(bebida_suco)
   print(prato_torrada)
    

if __name__ == '__main__':
    main()