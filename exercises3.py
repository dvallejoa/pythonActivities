def main():
    num1 = int(input("Introduce el primer valor para realizar el MCD: "))
    num2 = int(input("Introduce el segundo valor para realizar el MCD: "))

    if num1 > num2:
        A = num1
        B = num2
    else:
        A = num2
        B = num1

    while B:
        mcd = B
        B = A % B
        A = mcd

    print('El calculo del MCD entre {} y {} es {}'.format(num1, num2, mcd))


if __name__ == "__main__":
    main()