def main():
    # VARIABLES
    byte = 1048576  # Iniciador de la tabla de multiplicar
    megabytes = int(
        input("Introduce cuantos megabytes quieres convertir: "))  # Introduce valor de la opción por teclado
    # FIN VARIABLES

    if megabytes >= 1:  # Para evitar confusiones, realizo esto para que no se introduzcan valores decimales.
        print("Equivale a", byte * megabytes, "bytes")


if __name__ == "__main__":
    main()