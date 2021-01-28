def main():
    read = int(input("Introduce el número del cuál quieres saber sus variantes primas: "))
    x = 0
    i = 0
    j = 0

    for i in range(2, read + 1):
        prime = True
        for j in range(2, 11):
            if i == j:
                break
            elif i % j == 0:
                prime = False
        if prime == True:
            print(' ', i, end='')
            x += 1


if __name__ == "__main__":
    main()