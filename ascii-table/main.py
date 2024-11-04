#Variables globales

#Funciones
def run(start_code: int, end_code: int) -> None:
    # TODO
    contador = 0
    for codigo in range(start_code, end_code + 1):
        codigoFormateado = f"{codigo:03}"
        caracter = chr(codigo)
        print(f"{codigoFormateado} {caracter}", end=" ")
        contador +=1
        if contador % 5 == 0:
            print()
    
#Codigo principal 
# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
    run(33,47)