import args

#INCOMPLETO
#Variables globales
gcd_value = 0
#Funciones 
def run(a: int, b: int) -> int:
    # TODO
    global gcd_value
    #Variable local
    menor = min(a,b)
    gcd_value = 1
    for i in range(menor, 0 -1):
          if a % i == 0 and b % i == 0:
            gcd_value = i 
            break

    return gcd_value


#Codigo Principal
# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
    print(gcd_value)