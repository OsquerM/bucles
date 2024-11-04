def run(maxNum):
    # TODO
     for y in range(maxNum +1):
        fila = []
        for x in range(y ,maxNum + 1):
                fila.append(f"{x}|{y}")
        print("".join(fila))
    

# DO NOT TOUCH THE CODE BELOW
if __name__ == '__main__':
    import vendor

    vendor.launch(run)
    run(6)
