def validar_numero(mensaje, max=float("inf")):
    while True:
        nuevo_n = input(f"{mensaje}")
        if nuevo_n.isdigit():
            numero = int(nuevo_n)
            if numero <= max:
                return numero
            else:
                print(f"El número debe ser menor o igual a {max}.")
        else:
            print("Solo se permiten números enteros positivos. Intente de nuevo.")


def tiene_tilde(texto):
    tildes = "áéíóúÁÉÍÓÚ"
    set_tildes = set(tildes)

    for tilde in set_tildes:
        if tilde in texto:
            return True

    return False

def validar_palabra(mensaje):
    while True:
        texto = input(mensaje)
        if " " in texto:
            print("No se permiten espacios. Intente de nuevo.")
        elif tiene_tilde(texto):
            print("No se permiten tildes. Intente de nuevo.")
        elif texto == "":
            print("La entrada no puede estar vacía.")
        else:
            return texto
    
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Ejercicio 1
n = validar_numero("Ingresá un número entero positivo: ")

print("Factoriales del 1 al", n)
for i in range(1, n + 1):
    print(f"{i}! = {factorial(i)}")


# Ejercicio 2
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

pos = validar_numero("Mostrando serie de Fibonacci hasta la posición: ")
print("Serie de Fibonacci:")
for i in range(pos + 1):
    print(f"Posición ({i}) = {fibonacci(i)}")

# Ejercicio 3

def potencia(base, exponente):
    if exponente == 0:
        return 1
    return base * potencia(base, exponente - 1)

b = validar_numero("Base: ")
e = validar_numero("Exponente: ")
print(f"{b}^{e} = {potencia(b, e)}")

# Ejercicio 4

def a_binario(n):
    if n == 0:
        return ""
    return a_binario(n // 2) + str(n % 2)

numero = validar_numero("Número decimal a convertir en binario: ")
binario = a_binario(numero)
if(binario):
    print(f"Binario: {binario}")
else:
    print(f"Binario: 0")

# Ejercicio 5

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

texto = validar_palabra("Ingresá una palabra sin espacios ni tildes: ").lower()
print("¿Es palíndromo?", es_palindromo(texto))

# Ejercicio 6

def suma_digitos(n):
    if n < 10:
        return n
    return n % 10 + suma_digitos(n // 10)

numero = validar_numero("Número entero positivo: ")
print("Suma de dígitos:", suma_digitos(numero))

# Ejercicio 7

def contar_bloques(n):
    if n == 1:
        return 1
    return n + contar_bloques(n - 1)

nivel = validar_numero("Bloques en el nivel más bajo: ")
print("Total de bloques:", contar_bloques(nivel))

# Ejercicio 8

def contar_digito(numero, digito):
    if numero == 0:
        return 0
    return (1 if numero % 10 == digito else 0) + contar_digito(numero // 10, digito)

n = validar_numero("Número entero positivo: ")
d = validar_numero("Dígito a contar (0-9): ",9)
print(f"El dígito {d} aparece {contar_digito(n, d)} veces.")
