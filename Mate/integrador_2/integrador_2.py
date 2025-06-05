import os

# Cantidad máxima de DNIs a ingresar
MAX_DNIS = 2

def ingresar_dnis():
    print(f"\nDebe ingresar exactamente {MAX_DNIS} DNIs numéricos.")
    lista_dnis = []
    contador = 0
    while contador < MAX_DNIS:
        dni_ingresado = input(f"Ingrese DNI #{contador + 1}: ")
        # Validar que el DNI ingresado sea numérico
        if dni_ingresado.isdigit():
            lista_dnis += [dni_ingresado]
            contador += 1
        else:
            print("❌ Solo se permiten números. Intente de nuevo.")
    return lista_dnis

def generar_conjuntos_unicos(lista_dnis):
    # Crea un diccionario con los dígitos únicos ordenados de cada DNI
    diccionario_digitos = {}
    for dni in lista_dnis:
        digitos_unicos = []
        for digito in dni:
            if digito not in digitos_unicos:
                digitos_unicos += [digito]
        digitos_unicos.sort()  # Ordena los dígitos únicos
        diccionario_digitos[dni] = digitos_unicos
        print(f"DNI: {dni} -> Dígitos únicos: {digitos_unicos}")
    return diccionario_digitos

def calcular_operaciones_conjuntos(diccionario_digitos):
    lista_dnis = []
    for dni in diccionario_digitos:
        lista_dnis += [dni]

    # Inicialización de estructuras para operaciones
    union_digitos = []
    interseccion_digitos = []
    diferencia_simetrica = []

    # Inicializa intersección y diferencia simétrica con el primer DNI
    for digito in diccionario_digitos[lista_dnis[0]]:
        interseccion_digitos += [digito]
        diferencia_simetrica += [digito]

    # Construye la unión de todos los dígitos únicos
    for dni in lista_dnis:
        for digito in diccionario_digitos[dni]:
            if digito not in union_digitos:
                union_digitos += [digito]
    union_digitos.sort()

    # Calcula la diferencia individual de cada DNI respecto a los otros
    diferencias_individuales = {}
    for dni_base in lista_dnis:
        digitos_otro_dni = []
        for otro_dni in lista_dnis:
            if otro_dni != dni_base:
                for digito in diccionario_digitos[otro_dni]:
                    if digito not in digitos_otro_dni:
                        digitos_otro_dni += [digito]
        diferencia = []
        for digito in diccionario_digitos[dni_base]:
            if digito not in digitos_otro_dni:
                diferencia += [digito]
        diferencias_individuales[dni_base] = diferencia
    # Calcula intersección y diferencia simétrica entre los DNIs
    for dni in lista_dnis[1:]:
        nueva_interseccion = []
        for digito in interseccion_digitos:
            if digito in diccionario_digitos[dni]:
                nueva_interseccion += [digito]
        interseccion_digitos = nueva_interseccion

        nueva_simetrica = []
        for digito in diferencia_simetrica:
            if digito not in diccionario_digitos[dni]:
                nueva_simetrica += [digito]
        for digito in diccionario_digitos[dni]:
            if digito not in diferencia_simetrica:
                nueva_simetrica += [digito]
        diferencia_simetrica = nueva_simetrica

    interseccion_digitos.sort()
    diferencia_simetrica.sort()

    # Muestra los resultados de las operaciones con conjuntos
    print("\n--- Operaciones con conjuntos ---")
    print("Unión de todos los dígitos:", union_digitos)
    print("Intersección de todos los dígitos:", interseccion_digitos)
    for dni in diferencias_individuales:
        print(f"Diferencia de {dni} con los demás: {diferencias_individuales[dni]}")
    print("Diferencia simétrica:", diferencia_simetrica)

    return interseccion_digitos

def contar_frecuencia_digitos(lista_dnis):
    print("\n--- Frecuencia de dígitos ---")
    for dni in lista_dnis:
        frecuencia = {}
        for digito in dni:
            if digito in frecuencia:
                frecuencia[digito] += 1
            else:
                frecuencia[digito] = 1

        # Ordena el diccionario de frecuencias por clave (dígito) en orden ascendente
        frecuencia_ordenada = dict(sorted(frecuencia.items()))
        print(f"DNI {dni}: {frecuencia_ordenada}")

def sumar_digitos_dni(lista_dnis):
    print("\n--- Suma de dígitos ---")
    for dni in lista_dnis:
        suma_total = 0
        for digito in dni:
            suma_total += int(digito)
        print(f"DNI {dni}: suma total = {suma_total}")

def evaluar_condiciones(diccionario_digitos, interseccion_digitos):
    print("\n--- Evaluación de condiciones ---")
    # Revisa si un DNI tiene más de 6 dígitos únicos
    for dni in diccionario_digitos:
        if len(diccionario_digitos[dni]) > 6:
            print(f"DNI {dni}: Diversidad numérica alta")
    # Muestra los dígitos que se repiten en todos los DNIs en una sola línea
    if interseccion_digitos:
        print("Dígitos compartidos:", ", ".join(interseccion_digitos))

def procesar_dnis():
    lista_dnis = ingresar_dnis()
    diccionario_digitos = generar_conjuntos_unicos(lista_dnis)
    interseccion_digitos = calcular_operaciones_conjuntos(diccionario_digitos)
    contar_frecuencia_digitos(lista_dnis)
    sumar_digitos_dni(lista_dnis)
    evaluar_condiciones(diccionario_digitos, interseccion_digitos)

def procesar_fecha():
    print("\nAcá va la fecha")

def mostrar_menu():
    continuar = True
    while continuar:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Procesar DNIs")
        print("2. Procesar Fecha")
        print("0. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            procesar_dnis()
        elif opcion == "2":
            procesar_fecha()
        elif opcion == "0":
            print("Saliendo del programa.")
            continuar = False
        else:
            print("Opción no válida. Intente nuevamente.")

# Limpia la pantalla antes de iniciar el menú (según sistema operativo)
os.system('cls' if os.name == 'nt' else 'clear')
mostrar_menu()
