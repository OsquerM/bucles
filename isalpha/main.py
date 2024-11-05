#Variable global
isalpha = ""
ALPHABET = "abcdefghijklmnopqrstuvwxyz"
#Funciones
def run(text: str) -> bool:
    # TODO
    #Variable local
    salida = True
    for char in text:
        if char not in ALPHABET:
            print("No es alfabetica")
            salida = False
            break
    if salida:
        print("Es alfabetica")
    return salida
    

#Codigo principal
# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
    print(run("hello-world"))