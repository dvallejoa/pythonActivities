from __future__ import print_function

def main():
    aula = []
    aulas = []


    register = int(input("Introduce cuantos registros quieres: "))

    for x in range(register):
        print("*** Número de registro", x,"***")
        aula_id = int(input("Introduce el ID de la aula: "))
        aula.append(aula_id)
        while aula_id not in range(1,50):
            aula_id = int(input("Valor introducido no valido (1 a 50): "))
        aula_nom = input("Introduce el nombre del aula: ")
        aula_ips = input("Introduce la IP de tu ordenador: ")
        aula_pcs = int(input("Introduce el nombre de ordenadores: "))
        while aula_pcs not in range(1,20):
            aula_pcs = int(input("Valor introducido no valido (1 a 20): "))

        print("*** Registros almacenados ***")
        aulas.append([aula_id, aula_nom, aula_ips, aula_pcs])

    print("""+-----------------------------------------+ \nID     Nombre       IP               PCS \n+-----------------------------------------+""")
    for x in range(register):
        print(*aulas[x], sep="       ")



if __name__ == "__main__":
    main()

