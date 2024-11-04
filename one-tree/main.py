#Variables globales

#Funciones
def run():
    # TODO
    numeros = [int("1" * i) for i in range(1,10)]
    #Variable local
    for num in numeros:
            resultado = num * num
            print(f"{num} * {num} = {resultado}")
    return 

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
