def main():
    # VARIABLES
    tab_ini = 1  # Iniciador de la tabla de multiplicar
    value = 1  # Valores multiplicados de la tabla de multiplicar
    # FIN VARIABLES

    for tab_ini in range(11):
        print('\n')
        print("Tabla de multiplicar del ", tab_ini)
        for value in range(1, 11):
            print(tab_ini, " x ", value, "=", tab_ini * value)


if __name__ == "__main__":
    main()
