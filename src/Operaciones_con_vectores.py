import numpy as np


A = []
B = []
def definirVectores():
    global A
    global B
    A = []
    B = []
    print("\n------------------------------------------------\n")
    print("\nIngresa la dimension de los vectores: \n")
    dimA = input("\tdim A: ")
    dimB = input("\tdim B: ")

    print("\n\tIngresa los " + dimA + " valores de A: ")
    for x in range(0, int(dimA)):
        A.append(float(input("\t>")))

    print("\n\tIngresa los " + dimB + " valores de B: ")
    for x in range(0, int(dimB)):
        B.append(float(input("\t>")))


    print("\n\nVector A: ")
    print(A)
    print("\n\nVector B: ")
    print(B)

    A = np.asarray(A)
    B = np.asarray(B)
    print("\n------------------------------------------------\n")
    mainMenu()

def mostrarVectores():
    global A
    global B
    print("\n------------------------------------------------\n")
    print("Vector A: ")
    print(A)
    print("\n\nVector B: ")
    print(B)
    print("\n------------------------------------------------\n")
    mainMenu()

def mainMenu():
    global A
    global B
    print("\n\tFavor de elegir una opción:")
    print("\n\t- 1) Definir/cambiar los vectores A y B")
    print("\n\t- 2) Mostrar los vectores A y B")
    print("\n\t- 3) Suma")
    print("\n\t- 4) Resta")
    print("\n\t- 5) Producto por un escalar")
    print("\n\t- 6) Norma")
    print("\n\t- 7) Ángulo entre vectores")
    print("\n\t- 8) Salir")
    selection = int(input("\t>>> "))
    switcher = { 
        1: definirVectores,
        2: mostrarVectores,
        8: "salir" # No es una funcion
    }
    func = switcher.get(selection, lambda: mainMenu) #Si no existe la seleccion, se coloca "mainMenu" y se repite
    # Execute the function
    if func == mainMenu:
        print("\n\t-- ¡Opción inválida! --")

    if func == "salir":
        print("\n\t-- ¡Salir! --")
        exit()
        
    func()

mainMenu()