def main():
    a = int(input("Introduce un número para A: "))
    b = int(input("Introduce un número para B: "))


    print("*** INTERCAMBIANDO NÚMEROS ***")
    a, b = b, a
    print("*** NÚMEROS INTERCAMBIADOS ***\n\n*** NUEVOS RESULTADOS ***")
    print("Número A ahora es:", a)
    print("Número B ahora es:", b)

if __name__ == "__main__":
    main()

