def main():
    segundos = int(input("Introdueix els valors en segons: "))

    dias = segundos // (24 * 60 * 60)
    segundos = segundos % (24 * 60 * 60)  # resta de los días
    horas = segundos // (60 * 60)
    segundos = segundos % (60 * 60)  # resta de las horas
    minutos = segundos // 60
    segundos = segundos % 60  # resta de los minutos

    print("Días: {}   Horas: {}   Minutos: {}  Segundos: {}".format(dias, horas, minutos, segundos))


if __name__ == "__main__":
    main()