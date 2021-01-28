def main():
    x = int(input("Introduce el primer nombre: "))
    y = int(input("Introduce el segundo nombre: "))
    z = int(input("Introduce el tercer nombre: "))

    if x == y and x == z:
        print("Numeros repetidos:", x, y, z)
    else:
        print("Suma de numeros:", x + y + z)


if __name__ == "__main__":
    main()

