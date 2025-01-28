import random
import string
import sys


class GeneradorContraseñas:

    def __init__(self):
        # Definir los conjuntos de caracteres
        self.letras_mayus = string.ascii_uppercase  # "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.letras_minus = string.ascii_lowercase  # "abcdefghijklmnopqrstuvwxyz"
        self.numeros = string.digits  # "0123456789"
        self.simbolos = string.punctuation  # "!@#$%^&*()_+[]{},.<>?/|"

        # Diccionario de niveles

        self.niveles = {
            1: self.letras_mayus + self.letras_minus,  # Nivel 1: Solo letras
            2: self.letras_mayus + self.letras_minus + self.numeros,  # Nivel 2: Letras + Números
            3: self.letras_mayus + self.letras_minus + self.numeros + self.simbolos
            # Nivel 3: Letras + Números + Símbolos
        }

    def generar_contraseña(self, nivel, num_caracteres):
        if nivel not in self.niveles:  # si el nivel no esta en el diccionario de niveles
            print("Nivel no válido")
            return None
        else:
            caracteres = self.niveles[nivel]
            return ''.join(random.choices(caracteres, k=num_caracteres))

    def guardar_en_archivo(self, contraseña):
        with open('contraseñas.txt', 'a', encoding='utf8') as archivo:
            archivo.write(contraseña + '\n')
        print(f'Contraseña guardada en contraseñas.txt')

    def menu(self):
        while True:
            print('-----Generador de contraseñas-----')
            print('1. Crear contraseña')
            print('2. Salir del programa')

            try:
                opcion = int(input('Elige una opción del 1 al 2:'))

                if opcion == 1:
                    nivel = int(input('Elige un nivel de dificultad (1, 2, 3): '))
                    num_caracteres = int(input('Introduce el número de caracteres: '))

                    if num_caracteres < 5:
                        print('El número de caracteres debe ser al menos 6.')
                    else:
                        contraseña = self.generar_contraseña(nivel, num_caracteres)
                        print(f'Contraseña generada: {contraseña}')

                        # preguntamos si el usuario quiere guardar la contraseña
                        guardar = input('¿Desea guardar la contraseña (si/no)?')
                        if guardar == 'si':
                            self.guardar_en_archivo(contraseña)

                elif opcion == 2:
                    sys.exit('Saliendo del programa...')

                else:
                    print("Opción no válida. Intenta nuevamente.")

            except Exception as e:
                print(f'Error: {e}. Debes ingresar un número válido!')
