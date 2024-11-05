#Variable global
left_side = 0
right_side = 0

#Funciones
def run(n: int) -> tuple:
    # TODO
    global left_side, right_side
    #Variable local
    suma = sum(range (1, n +1))
    left_side = suma ** 2
    right_side = sum(k ** 3 for k in range(1 , n +1))

    if left_side == right_side:
         print(f"Para n = {n}, la igualdad se cumple: {left_side} = {right_side}")
    else:
        print(f"Para n = {n}, la igualdas no se cumple.")
    return left_side, right_side

#Codigo principal
# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
    print(left_side, right_side)