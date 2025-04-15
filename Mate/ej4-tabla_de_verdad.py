import os

# leer_entero_validado, recibe 1 parametro:
# un mensaje
# comprueba que el usuario haya ingresado solamente números
def validar_ingreso_numero(mensaje):
    while True:
        n = input(f"{mensaje}: ")
        try:
            numero = int(n)
            break
        except ValueError:
            print("Eso no es un número válido. Intente nuevamente.")

    return numero

# leer_entero_validado, recibe 3 parametros:
# un mensaje
# un valor minimo   -   "-Inf" por default
# un valor máximo   -   "Inf" por default
# comprueba que el usuario ingrese un número entre los valores minimos y maximos
def leer_entero_validado(mensaje, min = float("-Inf"), max = float("Inf")):
    numero = validar_ingreso_numero(mensaje)

    while numero < min or numero > max:
        print("Opción incorrecta. Ingrese un valor válido")
        numero = validar_ingreso_numero(mensaje)

    return numero

def tabla_verdad(operacion):
    # Impresión del principio de la tabla

    if operacion == 3:
        resultado_titulo = f"{opciones[operacion]} A"
        print(f"\nTabla de Verdad para: {resultado_titulo}\n")
        print(f" A | {resultado_titulo}")
        print(f"---|{'-' * len(resultado_titulo)  + '--'}")
    else:
        resultado_titulo = f"A {opciones[operacion]} B"
        print(f"\nTabla de Verdad para: {resultado_titulo}\n")
        print(f" A | B | {resultado_titulo}")
        print(f"---|---|{'-' * len(resultado_titulo)  + '--'}")

    for A in [0, 1]:
        if operacion == 3:
            print(f" {A} | {not(A):^{len(resultado_titulo)}}")
        else:
            for B in [0, 1]:
                if operacion == 1:
                    resultado = A and B
                elif operacion == 2:
                    resultado = A or B
                elif operacion == 4:
                    resultado = A ^ B
                elif operacion == 5:
                    resultado = int(not (A and B))
                elif operacion == 6:
                    resultado = int(not (A or B))
                elif operacion == 7:
                    if A and not B:
                        resultado = 1
                    else:
                        resultado = 0
                elif operacion == 8:
                    if A == B:
                        resultado = 1
                    else:
                        resultado = 0
                print(f" {A} | {B} | {str(resultado):^{len(resultado_titulo)}}")

def imprimir_menu(lista_menu, tiene_salir = False):
    print("\nOperaciones disponibles:")
    for op in lista_menu:
        print(f"{op} - {lista_menu[op]}")

    if tiene_salir:
        print("---------")
        print("0 - Salir\n")

# Objeto de opciones
opciones = {
    1: "AND",
    2: "OR",
    3: "NOT",
    4: "XOR",
    5: "NAND",
    6: "NOR",
    7: "IMPLICACION",
    8: "BICONDICIONAL"
}

opciones_continuar = {
    1: "SI",
    2: "NO",
}



def tabla_de_verdad():
    
    despedida = "¡Hasta luego!"
    # Menú en bucle
    
    while True:
        # Imprime de forma dinamica el menu de opciones para las tablas
        imprimir_menu(opciones, True)

        eleccion = leer_entero_validado("Selecciona una operación (0-7): ", 0, 8)
        if eleccion == 0:
            print(despedida)
            break

        tabla_verdad(eleccion)

        # Imprime de forma dinamica el menu de opciones para volver a ver
        imprimir_menu(opciones_continuar)
        ver_otra = leer_entero_validado("Desea ver otra tabla?: ", 1, 2)
        if ver_otra == 2:
            print(despedida)
            break

# Limpia la pantalla
os.system('cls' if os.name == 'nt' else 'clear')
tabla_de_verdad()