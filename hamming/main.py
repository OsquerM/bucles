#Variable global
dhamming = 0
#Funcion
def run(text1: str, text2: str) -> int:
    # TODO
    global dhamming
    #Variable local
    if len(text1) != len(text2):
        return -1
    distancia = 0
    for i in range(len(text1)):
        if text1[i] != text2[i]:
            distancia +=1
    return dhamming

#Codigo principal
# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor
    text1 = input("Introduce la primera cadena de texto: ")
    text2 = input("Introduce la segunda cadena de texto: ")
    vendor.launch(run)
    resultado = run(text1,text2)
    if resultado == -1:
        print("Las cadenas tienen diferente longitud.")
    else:
        print(f"La distancia de Hamming entre las cadenas es: {resultado}")