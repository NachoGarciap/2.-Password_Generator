import random
import string

# Definir los conjuntos de caracteres
letras_mayus = string.ascii_uppercase  # "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
letras_minus = string.ascii_lowercase  # "abcdefghijklmnopqrstuvwxyz"
numeros = string.digits  # "0123456789"
simbolos = string.punctuation  # "!@#$%^&*()_+[]{},.<>?/|"

# Unir todos los caracteres en una sola variable
todos_los_caracteres = letras_mayus + letras_minus + numeros + simbolos

# Pedir al usuario el numero de caracteres

while True:
    try:
        num_caracteres = int(input('Introduce el numero de caracteres: '))
        if num_caracteres < 5:
            print('El numero de caracteres debe contener un minimo de 6 caracteres.')
        else:
            break  # salimos del bucle si es valido

    except Exception as e:
        print('Error: Debes ingresar un numero valido!')

prueba = ''.join(random.choices(todos_los_caracteres, k=num_caracteres))

print(f'La contraseña es: {prueba}')
