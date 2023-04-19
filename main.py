import time

Ndiscos = 3
Ntiempo = 1  # tiempo en segundos de espera antes de mover otro disco


def hanoi(n, origen, destino, medio, tiempo):  # Función recursiva
    if n == 1:
        time.sleep(tiempo)
        print("Mover disco 1, desde: ", origen, " hasta ", destino)
        return
    hanoi(n - 1, origen, medio, destino, tiempo)  # pasar los dicso, excepto el último, a la torre de en medio
    time.sleep(tiempo)
    print("Mover disco: ", n, " desde: ", origen, " hasta: ", destino)
    hanoi(n - 1, medio, destino, origen, tiempo)  # pasar los discos del medio a la última torre


def menu():  # Función que limpia la pantalla y muestra nuevamente el menu
    print("Bienvenido. Seleccione una de las siguientes opciones")
    print("\t1 - Colocar el número de discos a utilizar")
    print("\t2 - El tiempo entre movimientos")
    print("\t3 - Simular")


def opciones():
    while True:
        global Ndiscos
        global Ntiempo

        menu()
        opcionMenu = input("Inserta el valor numérico de la opción >> ")

        if opcionMenu == "1":
            N = int(input("Ingrese el número de discos (debe ser un número natural entre 3 y 10, inclusives): "))
            if 3 <= N <= 10:
                Ndiscos = N
            else:
                print("Número incorrecto, por favor ingrese un número natural entre 3 y 10")
        elif opcionMenu == "2":
            M = int(input(
                "Ingrese el número de tiempo entre cada movimmiento (debe ser un número natural entre 1 y 10, inclusives): "))
            if 1 <= M <= 10:
                Ntiempo = M
            else:
                print("Número incorrecto, por favor ingrese un número natural entre 3 y 10")
        elif opcionMenu == "3":
            hanoi(Ndiscos, "A", "C", "B", Ntiempo)
        else:
            print("La opción que ingresó no es correcta \n")


opciones()
