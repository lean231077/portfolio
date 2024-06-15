class Tamagotchi:
    def __init__(self, nombre):
        self.nombre = nombre
        self.nivel_energia = 100
        self.nivel_hambre = 0
        self.nivel_felicidad = 50
        self.humor = "indiferente"
        self.esta_vivo = True

    def mostrar_estado(self):
        print(f"Nombre: {self.nombre}")
        print(f"Nivel de energía: {self.nivel_energia}")
        print(f"Nivel de hambre: {self.nivel_hambre}")
        print(f"Estado de humor: {self.humor}")

    def alimentar(self):
        self.nivel_hambre -= 10
        self.nivel_energia += 15
        self.verificar_estado()

    def jugar(self):
        self.nivel_felicidad += 20
        self.nivel_energia -= 18
        self.nivel_hambre += 10
        self.verificar_estado()

    def dormir(self):
        self.nivel_energia += 40
        self.nivel_hambre += 5
        self.verificar_estado()

    def verificar_estado(self):
        if self.nivel_hambre >= 20:
            self.nivel_energia -= 20
            self.nivel_felicidad -= 30
            if self.nivel_energia <= 0:
                self.esta_vivo = False
                print(f"{self.nombre} ha muerto de hambre!")
        if self.nivel_energia <= 0:
            self.esta_vivo = False
            print(f"{self.nombre} ha muerto de agotamiento!")
        if self.nivel_felicidad >= 80:
            self.humor = "eufórico"
        elif 50 <= self.nivel_felicidad < 80:
            self.humor = "feliz"
        elif 20 <= self.nivel_felicidad < 50:
            self.humor = "indiferente"
        elif 10 <= self.nivel_felicidad < 20:
            self.humor = "triste"
        else:
            self.humor = "enojado"



mi_tamagotchi = Tamagotchi("Tama")

while True:   
    
    print("\n Elija la opcion deseada")
    print("\n ------------------------")
    print("1. Mostrar estado")
    print("2. Alimentar")
    print("3. Jugar")
    print("4. Dormir")
    print("5. Salir")
    
    opcion = input("Selecciona una opción (1-5): ")
    
    if opcion == "1":
        mi_tamagotchi.mostrar_estado()
    elif opcion == "2":
        mi_tamagotchi.alimentar()
    elif opcion == "3":
        mi_tamagotchi.jugar()
    elif opcion == "4":
        mi_tamagotchi.dormir()
    elif opcion == "5":
        print("¡Adiós!")
        break
    else:
        print("Opción inválida. Intenta de nuevo.")
   # mi_tamagotchi.mostrar_estado()
    #mi_tamagotchi.alimentar()
    #mi_tamagotchi.mostrar_estado()
    #mi_tamagotchi.jugar()
    #mi_tamagotchi.mostrar_estado()
    #mi_tamagotchi.dormir()
    #mi_tamagotchi.mostrar_estado()
