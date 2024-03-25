from Modelos.restaurante import Restaurante
 
restaurante_praca = Restaurante('Praca', 'Gourmet')
#restaurante_mexicano = Restaurante('Mexican Food', 'Comida Mexicana')
#restaurante_japones = Restaurante('Japa Food', 'Japonesa')

restaurante_praca.receber_avaliacao('Gabriel', 10)
restaurante_praca.receber_avaliacao('Caroline', 5)
restaurante_praca.receber_avaliacao('Cleci', 7)

def main():
    Restaurante.listar_restaurantes()
    

if __name__ == '__main__':
    main()