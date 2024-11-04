#Variables Globales

#Funciones
def run(limit: int) -> None:
    # TODO
    #Variables locales
    suma = 0
    multiples = []
    i = 3  # Comenzamos desde el primer múltiplo de 3
    
    while suma < limit:
        multiples.append(i)  # Agregar el múltiplo a la lista
        suma += i  # Sumar el múltiplo
        i += 3  # Pasar al siguiente múltiplo de 3

    print("Múltiplos de 3:", multiples)
    print("Suma:", suma)
    return

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
