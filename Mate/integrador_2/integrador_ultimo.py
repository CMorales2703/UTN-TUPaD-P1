import os

# Función para ingresar una cantidad fija de DNIs desde teclado
def ingresar_dnis():
    lista_dnis = []
    contador = 0

    # Cantidad fija de DNIs a ingresar (puede ajustarse si se desea)
    cantidad_dnis = 2

    while contador < cantidad_dnis:
        dni_ingresado = input(f"Ingrese DNI #{contador + 1}: ")
        # Validar que el DNI ingresado sea numérico
        if dni_ingresado.isdigit():
            lista_dnis.append(dni_ingresado)
            contador += 1
        else:
            print("Solo se permiten números. Intente de nuevo.")
    return lista_dnis


# Función que genera los dígitos únicos de cada DNI ingresado
def generar_conjuntos_unicos(lista_dnis):
    diccionario_digitos = {}
    for i in range(len(lista_dnis)):
        dni = lista_dnis[i]
        digitos_unicos = []
        for j in range(len(dni)):
            digito = dni[j]
            if digito not in digitos_unicos:
                digitos_unicos.append(digito) 
        digitos_unicos.sort()  
        diccionario_digitos[dni] = digitos_unicos 
        print(f"DNI: {dni} -> Dígitos únicos: {digitos_unicos}")
    return diccionario_digitos


# Función que realiza operaciones de conjunto entre los DNIs: unión, intersección, diferencias
def calcular_operaciones_conjuntos(diccionario_digitos):
    # Asumimos diccionario_digitos: clave = DNI, valor = lista de dígitos únicos

    lista_dnis = list(diccionario_digitos.keys())

    # 1. Construimos la unión de dígitos únicos de todos los DNIs
    union = []
    for dni in lista_dnis:
        digitos_actuales = diccionario_digitos[dni]
        for digito in digitos_actuales:
            if digito not in union:
                union.append(digito)
    union.sort()

    # 2. Calculamos la diferencia individual de cada DNI con respecto a los demás
    diferencias_individuales = {}

    for dni_base in lista_dnis:
        # Recolectamos todos los dígitos de los demás DNIs
        digitos_otros = []
        for otro_dni in lista_dnis:
            if otro_dni != dni_base:
                for digito in diccionario_digitos[otro_dni]:
                    if digito not in digitos_otros:
                        digitos_otros.append(digito)

        # Buscamos los dígitos exclusivos del dni_base (que no estén en los otros)
        diferencia = []
        for digito in diccionario_digitos[dni_base]:
            if digito not in digitos_otros:
                diferencia.append(digito)

        diferencias_individuales[dni_base] = diferencia

    # 3. Inicializamos la intersección y diferencia simétrica con los dígitos del primer DNI
    primer_dni = lista_dnis[0]
    interseccion = []
    diferencia_simetrica = []

    for digito in diccionario_digitos[primer_dni]:
        interseccion.append(digito)
        diferencia_simetrica.append(digito)

    # 4. Calculamos la intersección y diferencia simétrica entre todos los DNIs uno a uno
    for dni in lista_dnis[1:]:
        # Intersección: dígitos que están en intersección y en el DNI actual
        nueva_interseccion = []
        for digito in interseccion:
            if digito in diccionario_digitos[dni]:
                nueva_interseccion.append(digito)
        interseccion = nueva_interseccion

        # Diferencia simétrica: elementos en diferencia_simetrica pero no en el dni actual,
        # más elementos en el dni actual que no están en diferencia_simetrica
        nueva_simetrica = []
        for digito in diferencia_simetrica:
            if digito not in diccionario_digitos[dni]:
                nueva_simetrica.append(digito)

        for digito in diccionario_digitos[dni]:
            if digito not in diferencia_simetrica:
                nueva_simetrica.append(digito)
        diferencia_simetrica = nueva_simetrica

    # Ordenamos resultados para mayor claridad
    interseccion.sort()
    diferencia_simetrica.sort()

    # Resultados
    print("Unión de dígitos:", union)
    print("Intersección de dígitos:", interseccion)
    print("Diferencias individuales:", diferencias_individuales)
    print("Diferencia simétrica:", diferencia_simetrica)

    return interseccion

# Función que cuenta la frecuencia de cada dígito en cada DNI
def contar_frecuencia_digitos(lista_dnis):
    print("\n--- Frecuencia de dígitos ---")
    for i in range(len(lista_dnis)):
        dni = lista_dnis[i]
        frecuencia = {}
        for j in range(len(dni)):
            digito = dni[j]
            if digito in frecuencia:
                frecuencia[digito] += 1
            else:
                frecuencia[digito] = 1
        frecuencia_ordenada = dict(sorted(frecuencia.items()))
        print(f"DNI {dni}: {frecuencia_ordenada}")


# Función que suma todos los dígitos de cada DNI
def sumar_digitos_dni(lista_dnis):
    print("\n--- Suma de dígitos ---")
    for i in range(len(lista_dnis)):
        dni = lista_dnis[i]
        suma_total = 0
        for j in range(len(dni)):
            suma_total += int(dni[j])  # Convierte el carácter a entero
        print(f"DNI {dni}: suma total = {suma_total}")


# Función que evalúa condiciones como diversidad numérica o dígitos comunes
def evaluar_condiciones(diccionario_digitos, interseccion_digitos):
    print("\n--- Evaluación de condiciones ---")
    claves = list(diccionario_digitos.keys())
    for i in range(len(claves)):
        dni = claves[i]
        if len(diccionario_digitos[dni]) >= 5:
            print(f"DNI {dni}: Diversidad numérica alta")  # Al menos 5 dígitos únicos
    if interseccion_digitos:
        print("Dígitos compartidos:", ", ".join(interseccion_digitos))


# Función principal que coordina todas las funciones anteriores
def procesar_dnis():
    lista_dnis = ingresar_dnis()
    diccionario_digitos = generar_conjuntos_unicos(lista_dnis)
    interseccion_digitos = calcular_operaciones_conjuntos(diccionario_digitos)
    contar_frecuencia_digitos(lista_dnis)
    sumar_digitos_dni(lista_dnis)
    evaluar_condiciones(diccionario_digitos, interseccion_digitos)


def procesar_fecha():
    
    # Ejercicio 1: Ingreso de los años de nacimiento
    # Si dos o más integrantes del grupo tienen el mismo año, se modifica con un dato ficticio

    años_nacimiento = []

    # Pedimos la cantidad de integrantes del grupo
    cantidad = int(input("\n¿Cuántos integrantes hay en el grupo?: "))

    # Cargamos los años de nacimiento
    for i in range(cantidad):
        año = int(input(f"Ingresá el año de nacimiento del integrante {i+1}: "))
        
        # Si el año ya fue ingresado, se suma 1 hasta que sea único
        while año in años_nacimiento:
            print("Ese año ya fue ingresado. Se usará un año ficticio (+1).")
            año += 1
        
        años_nacimiento.append(año)

    # Convertimos la lista a conjunto para eliminar duplicados
    años_nacimiento = set(años_nacimiento)

    print("\nAños de nacimiento ingresados:", años_nacimiento)

    # Ejercicio 2: Contar cuántos nacieron en años pares e impares

    pares = 0
    impares = 0

    # Recorremos cada año para contar pares e impares
    for año in años_nacimiento:
        if año % 2 == 0:
            pares += 1
        else:
            impares += 1

    print(f"\nNacidos en años pares: {pares}")
    print(f"\nNacidos en años impares: {impares}")

    # Ejercicio 3: Mostrar "Grupo Z" si todos nacieron después del año 2000

    if all(año > 2000 for año in años_nacimiento):
        print("\nGrupo Z")

    # Ejercicio 4: Mostrar "Tenemos un año especial" si alguno nació en un año bisiesto

    # Función para determinar si un año es bisiesto
    def es_bisiesto(año):
        return (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0)

    # Verificamos si hay al menos un año bisiesto
    if any(es_bisiesto(año) for año in años_nacimiento):
        print("Tenemos un año especial")

    # Ejercicio 5: Función para determinar si un año es bisiesto

    def es_bisiesto(año):
        
        #Devuelve True si el año es bisiesto, False si no lo es.
        
        return (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0)

    # Ejercicio 6: Calcular el producto cartesiano entre los años y las edades actuales

    from datetime import datetime
    from itertools import product

    # Obtener el año actual automáticamente
    año_actual = datetime.now().year

    # Calcular el conjunto de edades
    edades = {año_actual - año for año in años_nacimiento}
    print("\nEdades actuales:", edades)

    # Calcular el producto cartesiano entre años y edades
    producto_cartesiano = list(product(años_nacimiento, edades))

    # Mostrar los pares ordenados
    print("\nProducto cartesiano (año de nacimiento, edad):")
    for par in producto_cartesiano:
        print(par)

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
