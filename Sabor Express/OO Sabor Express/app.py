from Modelos.restaurante import Restaurante
    
restaurante_praca = Restaurante('Praca', 'Gourmet')
restaurante_mexicano = Restaurante('Mexican Food', 'Comida Mexicana')
restaurante_japones = Restaurante('Japa Food', 'Japonesa')

restaurante_mexicano.alternar_estado()

def main():    
    Restaurante.listar_restaurantes()
    

if __name__ == '__main__':
    main()