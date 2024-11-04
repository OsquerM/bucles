#Variables globales
movements = 0
#Funciones
def run(target_x: int, target_y: int) -> int:
    # TODO
    global movements
    #Variable local
    x , y = 0 , 0
    if (target_x + target_y) % 3 != 0:
        return -1
    while x < target_x or y < target_y:
        # Realizamos el primer movimiento
        x += 2
        y += 1
        movements += 1
        if x >= target_x and y >= target_y:
            return movements
        
        # Realizamos el segundo movimiento
        x += 1
        y += 2
        movements += 1

        # Comprobamos nuevamente
        if x >= target_x and y >= target_y:
            return movements
    return -1

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
    resultado = run(5, 4)
    print(f"Movimientos necesarios para llegar a (5, 4): {resultado}")