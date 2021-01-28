def main():
    # VARIABLES
    polzades = 0.39  # Valor real de un centimetro en pulgadas
    cm = int(input(
        "Introduce cuantos centimetros quieres convertir: "))  # Valor introducido por teclado de cuantos centimetros a convertir
    # FIN VARIABLES

    print("Equivale a", (cm * polzades), "pulgadas")


if __name__ == "__main__":
    main()