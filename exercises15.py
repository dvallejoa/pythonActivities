def main():
    x = [10,20,30,20,10,50,60,40,80,50,40]
    y = []#empty

    print("Lista de numeros duplicados: ", x)
    y = set(x)
    print("La misma lista pero sin números duplicados: ", y)

if __name__ == "__main__":
    main()