def main():
    n = 15
    i = 0
    apf = 0
    suspf = 0
    counta = 0
    counts = 0

    for i in range(n):
        note = int(input("Introduce un número que se situe entre el 0 i el 10: "))
        if note < 11:
            i += 1
        else:
            note = int(input("El número introducido no está entre el 0 i el 10, introduce otro número: "))

        if note > 4:
            apf += 1
            counta += note
        else:
            suspf += 1
            counts += note

    aprob = (counta / apf) if apf != 0 else 0
    susp = (counts / suspf) if suspf != 0 else 0
    print("Media decimal de notas aprobadas ", aprob)
    print("Media decimal de notas suspendidas ", susp)
    print("Personas que han aprobado ", apf)
    print("Persones que han suspendido: ", suspf)


if __name__ == "__main__":
    main()

