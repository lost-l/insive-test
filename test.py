# Importaciones necesarias para la ejecucion del codigo. 
# --no es necesario instalar ninguna dependencia--
# 
# Usadas para:
# itertools → Se usa para poder saber las combinaciones posibles del alfabeto
# string → Para traer las letras minusculas del alfabeto
# re → Para realizar la validacion regex

import itertools
import string
import re

encrypted_message = [33, 4, 14, 26, 4, 8, 6, 18, 3, 4, 17, 83, 32, 20, 11, 31, 11, 4, 16, 30, 8, 65, 35, 29, 3, 19, 7, 0, 71, 35, 16, 26, 4, 4, 12, 28, 71, 50, 11, 16, 6, 2, 10, 95, 71, 9, 3, 0, 71, 13, 13, 20, 21, 0, 6, 28, 71, 5, 7, 0, 4, 8, 4, 1, 6, 19, 66, 22, 11, 65, 15, 22, 9, 18, 3, 25, 2, 79, 66, 83, 38, 9, 13, 1, 6, 77, 66, 3, 6, 19, 3, 83, 22, 20, 7, 83, 46, 15, 17, 26, 17, 4, 66, 1, 2, 2, 13, 29, 8, 27, 1, 18, 71, 21, 23, 83, 11, 14, 5, 1, 8, 77, 66, 0, 18, 3, 7, 83, 2, 13, 66, 16, 8, 5, 7, 83, 4, 14, 12, 83, 2, 13, 66, 2, 18, 4, 66, 1, 2, 18, 13, 31, 17, 8, 17, 7, 2, 65, 7, 0, 19, 4, 66, 22, 13, 4, 16, 16, 14, 2, 11, 28, 71, 4, 12, 83, 32, 8, 22, 59, 18, 3, 77, 52, 14, 21, 46, 18, 5, 65, 27, 83, 4, 14, 15, 3, 6, 19, 22, 22, 71, 4, 14, 83, 2, 15, 14, 18, 4, 4, 66, 18, 71, 18, 13, 3, 8, 19, 22, 22, 39, 8, 12, 0, 14, 23, 7, 93, 4, 13, 76]


def get_combination():
    """
    Esta funcion permite saber cual es la combinacion que se debe usar para poder descifrar el mensaje encriptado, adicionalmente, muestra dicho mensaje al concluir su ejecucion
    """
    
    # En este punto, se obtiene las posibles combinaciones del alfabeto en un grupo de 4
    for combination in itertools.product(string.ascii_lowercase, repeat=4):
        
        # Variables de control
        flag, message, letter_idx = True, "", 0

        # Bucle que itera sobre cada uno de los numeros del mensaje encriptado
        for encrypted_ascii_number in encrypted_message:
            
            #  Obtiene el numero ascii de la letra del alfabeto en cuestion
            letter_ascii_number = ord(combination[letter_idx])
            
            # Realiza el 'cifrado' o 'descifrado' (XOR) 
            # entre el numero ascii del alfabeto y el actual numero del mensaje encriptado
            # No obstante, obtiene el caracter, en base al resultado del XOR.
            char = chr(letter_ascii_number ^ encrypted_ascii_number)
            
            # Verifica que se cumpla la Regex propuesta en la prueba
            if not re.fullmatch(r'[a-zA-Z0-9\s.,@\-_\/]', char):
                flag = False
                break
            
            # Adiciona cada caracter para poder visualizar el mensaje posteriormente.
            message += char
            
            # Variables de control
            if letter_idx > 2: letter_idx = -1
            letter_idx += 1
            
        # Por ultimo, muestra tanto la combinacion del alfabeto como el mensaje,
        # Si se encontro, los despliega en la terminal
        if flag:
            print(f'\n{combination}')
            print(message)
            
            
if __name__ == '__main__':
    get_combination()