#Variable global
result = 1
#Funcion
def run(n: int) -> int:
    # TODO
    global result
    #Variable local
    for i in range(1, n + 1):
        result *= i ** 2
    return result

#Codigo principal
# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
    print(result)
