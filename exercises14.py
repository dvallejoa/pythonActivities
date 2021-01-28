def main():
    x = int(input("Introduce cuantos números quieres introducir: "))
    lista = []
    i = 0
    for i in range(x):
        valor = int(input("Introduce un número: "))
        lista.append(valor)

    print("El resultado de la suma de los", x ,"números introducidos es", sum(lista))

if __name__ == "__main__":
    main()

