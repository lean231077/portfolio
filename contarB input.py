import colorama
from colorama import Fore, Style
import pyfiglet
#iniciar Banner de Bienvenida
colorama.init(autoreset=True)
def print_banner(text):
    banner = pyfiglet.figlet_format(text)
    print(Fore.CYAN + banner)

def input_with_prompt(prompt):
    print(Fore.GREEN + Style.BRIGHT + prompt, end='')
    return input(Fore.YELLOW)

print_banner("Bienvenido")
print ("ingresa una serie de letras B separadas por un punto para que la lista sea válida")

#Entrada de datos
cadena = input_with_prompt("Por favor, introduce la lista a verificar: ")
 
def verificar_lista(cadena): #verifica que solo se ingresen puntos y B
    
    for elemento in cadena:
        if elemento != '.' and elemento != 'B':
            print("Error: La lista contiene elementos no permitidos. Solo usa 'B' o '.'")
            return False
            
# Verificar que la lista tenga al menos dos elementos para las siguientes condiciones
        elif len(cadena) < 2:
            print("Error: La lista debe contener al menos dos elementos.")
            return False
    
# Verificar que el primer elemento sea '.' o 'B'
        elif cadena[0] != '.' and cadena[0] != 'B':
            print("Error: El primer elemento debe ser '.' o 'B'.")
            return False
#Inicializar el índice
    i = 1

    # Bucle while para comparar elementos consecutivos
    while  i < len(cadena):
        if cadena[i] == cadena[i - 1]:
            print("Error: Hay dos elementos iguales consecutivos. Las letras B deben estar separadas por un punto")
            return False
        i += 1
    print("La lista es válida.")
    return True
#iniciar verificación   
verificar_lista(cadena)