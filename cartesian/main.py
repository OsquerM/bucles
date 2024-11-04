#Variable global
cartesian = ""
#Funcion
def run(text1: str, text2: str) -> str:
    # TODO
    global cartesian
    #Variable local
    for palabra1 in text1:
        for palabra2 in text2:
            cartesian += text1 + text2
    return cartesian

#Codigo principal
# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
    print(cartesian)