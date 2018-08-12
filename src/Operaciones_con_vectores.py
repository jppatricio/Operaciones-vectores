import numpy as np
import math
from numpy import linalg as la


A = []
B = []
def igualarDim():
    if (len(A)) < (len(B)):
        A.resize(B.shape)
        print("Se igualaron la dimensiones")
    elif (len(B)) < (len(A)): #elif es else if en python
        B.resize(A.shape)
        print("Se igualaron la dimensiones")

def definirVectores():
    # Se obtienen las variables globales
    global A
    global B
    # Se reinicializan como vacios
    A = []
    B = []
    print("\n------------------------------------------------\n")
    print("\nIngresa la dimension de los vectores: \n")
    dimA = input("\tdim A: ")
    dimB = input("\tdim B: ")

    try:
        print("\n\tIngresa los " + dimA + " valores de A: ")
        for x in range(0, int(dimA)):
            A.append(float(input("\t>")))

        print("\n\tIngresa los " + dimB + " valores de B: ")
        for x in range(0, int(dimB)):
            B.append(float(input("\t>")))
    except:
        print("Favor de poner valores correctos (floats)")
        definirVectores()
        return

    print("\n\nVector A: ")
    print(A)
    print("\n\nVector B: ")
    print(B)

    # Se cambian de listas a arreglos de numpy (para realizar las operaciones en los metodos importados de NumPy)
    A = np.asarray(A)
    B = np.asarray(B)
    print("\n------------------------------------------------\n")

def mostrarVectores():
    global A
    global B
    print("\n------------------------------------------------")
    print("Vector A: ")
    print(A)
    print("\n\nVector B: ")
    print(B)
    print("------------------------------------------------\n")

def sumaVectores():
    global A
    global B

    # Si las dimensiones son distintas, se agregan 0's para igualar dimensiones--
    igualarDim()
    # ---------------------------------------------------------------------------

    print("\n-------------- SUMA ---------------\n")
    print("\n\t- 1) A + B")
    print("\n\t- 2) B + A")
    selection = ""
    try:
        selection = int(input("\t>>> "))
    except ValueError:
        print("Favor de elegir las opciones mostradas con enteros (Ej: 1)")

    switcher = { # Esta es la opción de python para un switch/case
        1: A+B,
        2: B+A
    }
    # switcher.get(opcionElegida, DefaultValue)
    func = switcher.get(selection, sumaVectores) #Si no existe la seleccion, se coloca mainMenu (es el default de python)

    # Si se escogió una opción inválida, se checa que func no sea un arreglo de numpy (si no, es una opción inválida)
    # y func es sumaVectores para repetir:
    if type(func) != np.ndarray and func == sumaVectores:
        print("\n\t-- Opción inválida... --")
        func()
    print("\tEl resultado es: ", func)
    input("\n\tPresione enter para continuar... ")
    
    print("\n------------------------------------------------\n")
    
def restaVectores():
    global A
    global B

    
    # Si las dimensiones son distintas, se agregan 0's para igualar dimensiones--
    igualarDim()
    # ---------------------------------------------------------------------------

    print("\n-------------- RESTA ---------------\n")
    print("\n\t- 1) A - B")
    print("\n\t- 2) B - A")
    selection = ""
    try:
        selection = int(input("\t>>> "))
    except ValueError:
        print("Favor de elegir las opciones mostradas con enteros (Ej: 1)")

    switcher = { # Esta es la opción de python para un switch/case
        1: A-B,
        2: B-A
    }
    # switcher.get(opcionElegida, DefaultValue)
    func = switcher.get(selection, sumaVectores) #Si no existe la seleccion, se coloca mainMenu (es el default de python)

    # Si se escogió una opción inválida, se checa que func no sea un arreglo de numpy (si no, es una opción inválida)
    # y func es sumaVectores para repetir:
    if type(func) != np.ndarray and func == sumaVectores:
        print("\n\t-- Opción inválida... --")
        func()
    print("\tEl resultado es: ", func)
    input("\n\tPresione enter para continuar... ")
    
    print("\n------------------------------------------------\n")

def productoEscalar():
    global A
    global B
    
    
    # Si las dimensiones son distintas, se agregan 0's para igualar dimensiones--
    igualarDim()
    # ---------------------------------------------------------------------------

    print("\n-------------- Multiplicación por escalar ---------------\n")
    print("\n\t- 1) xA")
    print("\n\t- 2) xB")
    selection = ""
    try:
        selection = int(input("\t>>> "))
    except ValueError:
        print("Favor de elegir las opciones mostradas con enteros (Ej: 1)")

    print("\n\t escribe el escalar:")
    escalar = ""
    try:
        escalar = float(input("\t>>> "))
    except ValueError:
        print("Favor de elegir el escalar con enteros decimales (Ej: 1.111)")

    switcher = { # Esta es la opción de python para un switch/case
        1: A*escalar,
        2: B*escalar
    }
    # switcher.get(opcionElegida, DefaultValue)
    func = switcher.get(selection, sumaVectores) #Si no existe la seleccion, se coloca mainMenu (es el default de python)

    # Si se escogió una opción inválida, se checa que func no sea un arreglo de numpy (si no, es una opción inválida)
    # y func es sumaVectores para repetir:
    if type(func) != np.ndarray and func == sumaVectores:
        print("\n\t-- Opción inválida... --")
        func()
    print("\tEl resultado es: ", func)
    input("\n\tPresione enter para continuar... ")

    
    print("\n------------------------------------------------\n")

def normaVector():
    global A
    global B
    
    # Si las dimensiones son distintas, se agregan 0's para igualar dimensiones--
    igualarDim()
    # ---------------------------------------------------------------------------

    print("\n-------------- Norma ---------------\n")
    print("\n\t- 1) A")
    print("\n\t- 2) B")
    selection = ""
    try:
        selection = int(input("\t>>> "))
    except ValueError:
        print("Favor de elegir las opciones mostradas con enteros (Ej: 1)")

    switcher = { # Esta es la opción de python para un switch/case
        1: la.norm(A),
        2: la.norm(B)
    }
    # switcher.get(opcionElegida, DefaultValue)
    func = switcher.get(selection, sumaVectores) #Si no existe la seleccion, se coloca mainMenu (es el default de python)

    # Si se escogió una opción inválida, se checa que func no sea un arreglo de numpy (si no, es una opción inválida)
    # y func es sumaVectores para repetir:
    if type(func) != np.ndarray and func == sumaVectores:
        print("\n\t-- Opción inválida... --")
        func()
    print("\tEl resultado es: ", func)
    input("\n\tPresione enter para continuar... ")

    
    print("\n------------------------------------------------\n")

def anguloVectores():
    print("\n-------------- Ángulo entre vectores ---------------\n")
    
    # Si las dimensiones son distintas, se agregan 0's para igualar dimensiones--
    igualarDim()
    # ---------------------------------------------------------------------------
    try:
        cosang = np.dot(A, B)
        sinang = la.norm(np.cross(A, B))
        func = np.arctan2(sinang, cosang)
        funcdeg = np.rad2deg(func)
    except ValueError:
        print("El valor maximo en dimensiones debe ser de 3")
        func = "ERROR"
    
    print("\tEl resultado (rad) es: ", func)
    print("\tEl resultado (deg) es: ", funcdeg)
    input("\n\tPresione enter para continuar... ")

    
    print("\n------------------------------------------------\n")

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
    selection = ""
    # El try es para que solo se puedan seleccionar números enteros (las opciones del menu)
    try:
        selection = int(input("\t>>> "))
    except ValueError:
        print("Favor de elegir las opciones mostradas con enteros (Ej: 1)")
    
    # Esta es la opción de python para un switch/case
    switcher = { 
        1: definirVectores,
        2: mostrarVectores,
        3: sumaVectores,
        4: restaVectores,
        5: productoEscalar,
        6: normaVector,
        7: anguloVectores,
        8: "salir" # No es una funcion
    }
    # switcher.get(opcionElegida, DefaultValue)
    func = switcher.get(selection, mainMenu) #Si no existe la seleccion, se coloca mainMenu

    # Si se eligió salir, entra al if y acaba el programa
    if func == "salir":
        print("\n\t-- Saliendo... --")
        exit()
    # Si se escogió una opción inválida, repite el menú con un print de "opcion inválida"
    if func == mainMenu:
        print("\n\t-- Opción inválida... --")

    # Si no es salir, se corre la funcion elegida:
    func()

# Se inicia corriendo mainMenu()

while True:
    mainMenu()