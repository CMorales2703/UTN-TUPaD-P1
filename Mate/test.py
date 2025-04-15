def leer_binario_validado(mensaje):

    while True:
        numero = input(f"{mensaje}")
        es_binario = True
        for i in numero:
            if i != "0" and i != "1":
                print("No es binario. Intenta de nuevo.")
                es_binario = False
                break
        if es_binario:
            return numero

def binario_a_decimal(numero_binario):
    cont = 0
    total = 0
    for i in reversed(numero_binario):
        total += int(i) * (2 ** cont)
        cont += 1
    
    return total

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

def decimal_a_binario(numero):
    binario = ""
    
    while numero > 0:
        resto = numero % 2
        binario = str(resto) + binario  
        numero = numero // 2  
    
    return binario if binario else "0"  

numero_binario = leer_binario_validado("Ingrese un número binario: ")
numero_decimal = binario_a_decimal(numero_binario)

numero = leer_entero_validado("Ingrese un número natural: ", 0)
decimal_binario = decimal_a_binario(numero)

print("Número binario:", numero_binario)
print("Número decimal:", numero_decimal)

print("Número decimal 2:", numero)
print("Número binario 2:", decimal_binario)