#Variables globales

#Funciones
def run(target_number: int) -> None:
    # TODO
    #Variables locales
    intentos = 0
    adivinado = False

    print("Comienza el juego")
    while not adivinado:
        target_number = int(input("Introduzca número: "))
        # Solicitar al usuario que introduzca su intento
        intento = int(input("Otro intento: "))
        intentos += 1  # Incrementar el contador de intentos
        
        # Comparar el intento con el número a adivinar
        if intento < target_number:
            print("El número buscado es mayor.")
        elif intento > target_number:
            print("El número buscado es menor.")
        else:
            adivinado = True  # Si adivina, cambia a True
            print(f"¡Felicidades! Has adivinado el número {target_number} en {intentos} intentos.")



#Codigo principal
# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
    run()