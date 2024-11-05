#Variables globales
fibo  = 0

#Funcion
def run(n: int) -> float:
    # TODO
    global fibo
    #Variable local
    a, b = 0, 1
    if n == 0:
        fibo = a
    elif n == 1:
        fibo = b
    else:
        for i in range(2, n +1):
            a , b = b, a + b
            fibo = b
    return fibo

#Codigo principal
# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
    print(f"El termino de Fibonacci es {fibo}")