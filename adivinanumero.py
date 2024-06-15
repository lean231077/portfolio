import random

def jugar_adivina_numero():
    
    numero_secreto = random.randint(1, 100)
    vidas = 5
    
    while vidas > 0:
        intento = int(input("Ingrese un número: "))
        
        if intento == numero_secreto:
            print("Has ganado", numero_secreto)
            return
        
        if intento < numero_secreto:
            print("El número es mayor.")
        else:
            print("El número es menor.")
        
        vidas -= 1
        
    
    print("El número secreto era:", numero_secreto)


jugar_adivina_numero()