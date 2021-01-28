def main():
    x = 10  # repetidor range y divisor 10
    value = 0  # repetidor almacen
    i = 0  # repetidor

    for i in range(x):
        y = int(input("Introdueix els valors:"))
        value += y
        i += 1
    print(value / x)


if __name__ == "__main__":
    main()
