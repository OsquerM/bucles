#Variables globales

#Funciones
def run():
    # TODO
     salir = True
     while salir: 
        nombre = input("Introduce tu nombre: ")
        if nombre == "oscar":
             print("Nombre escrito correctamente")
             salir = False
        else:
             print("Error. Debe escribirlo correctamente")
             
     return


#Codigo Principal
# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
