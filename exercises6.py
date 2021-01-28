def main():
    # VARIABLES
    a = 0  # Variable de almacen del número introducido
    # FIN VARIABLES
    print("Introduce un número entre el 0 hasta el 10")
    a = int(input("Introduce el número aquí: "))  # Introduce valor de la opción por teclado

    while a > 10:
        print("Introduce un número entre el 0 hasta el 10")
        a = int(input("Introduce el número aquí: "))  # Introduce valor de la opción por teclado
        print("El número introducido es", a)  # Valor único número 1 (a)


if __name__ == "__main__":
    main()

