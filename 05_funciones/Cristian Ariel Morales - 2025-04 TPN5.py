import utils
import math

print("\n--- Imprimir 'Hola Mundo' ---")
# Funciones
def printHelloWorld():
    print("Hola Mundo!")

# Programa Principal
printHelloWorld()


print("\n--- Saludo Personalizado al Usuario ---")
# Funciones
def greetUser(name):
    print(f"Hola {name}!")

# Programa Principal
name = input("Ingrese su nombre: ")
greetUser(name)


print("\n--- Mostrar Información Personal del Usuario ---")
# Funciones
def personalInfo(name, lastname, age, residence):
    print(f"Soy {name} {lastname}, tengo {age} años y vivo en {residence}")

# Programa Principal
name = input("Ingrese su nombre: ")
lastname = input("Ingrese su apellido: ")
age = input("Ingrese su edad: ")
residence = input("Ingrese su lugar de residencia: ")
personalInfo(name, lastname, age, residence)


print("\n--- Calcular Área y Perímetro de un Círculo ---")
# Funciones
def calculateCircleArea(r):
    return math.pi * (r**2)

def calculateCirclePerimeter(r):
    return 2 * math.pi * r

# Programa Principal
radio = float(input("Ingrese el radio: "))
area = calculateCircleArea(radio)
perimeter = calculateCirclePerimeter(radio)
print(f"El Area es: {area}")
print(f"El Perimetro es: {perimeter}")


print("\n--- Convertir Segundos a Horas ---")
# Funciones
def secondsToHours(segundos):
    hourInSecond = 3600
    return segundos / hourInSecond

# Programa Principal
seconds = utils.leer_entero_validado("Ingrese los segundos", 0)
horas = secondsToHours(seconds)
print(f"{seconds} segundos son {horas:.2f} horas.")


print("\n--- Mostrar Tabla de Multiplicar ---")
# Funciones
def multiplicationTable(number):
    for i in range(1, 10 + 1):
        print(f"{number} x {i} = {number * i}")

# Programa Principal
num = utils.leer_entero_validado("Ingrese un número")
multiplicationTable(num)


print("\n--- Operaciones Básicas entre Dos Números ---")
# Funciones
def basicOperations(num1, num2):
    sum = num1 + num2
    res = num1 - num2
    mult = num1 * num2
    if num2 != 0:
        div = num1 / num2
    else:
        div = "No se puede dividir por 0"
    return (sum, res, mult, div)

# Programa Principal
num1 = utils.leer_entero_validado("Ingrese el primer número")
num2 = utils.leer_entero_validado("Ingrese el segundo número")
sum, res, mult, div = basicOperations(num1, num2)
print(f"Suma: {sum}")
print(f"Resta: {res}")
print(f"Multiplicación: {mult}")
print(f"División: {div}")


print("\n--- Calcular Índice de Masa Corporal (IMC) ---")
# Funciones
def calculateBmi(peso, altura):
    return peso / (altura ** 2)

# Programa Principal
weight = utils.leer_decimal_validado("Ingrese el peso (en Kg)", 1)
height = utils.leer_decimal_validado("Ingrese la altura (en mtrs)", 1)
IMC = calculateBmi(weight, height)
print(f"Peso: {weight}")
print(f"Altura: {height}")
print(f"IMC: {IMC:.2f}")


print("\n--- Calcular Índice de Masa Corporal (IMC) (Repetido) ---")
# Funciones
def calculateBmi(peso, altura):
    return peso / (altura ** 2)

# Programa Principal
weight = utils.leer_decimal_validado("Ingrese el peso (en Kg)", 1)
height = utils.leer_decimal_validado("Ingrese la altura (en mtrs)", 1)
IMC = calculateBmi(weight, height)
print(f"Peso: {weight}")
print(f"Altura: {height}")
print(f"IMC: {IMC:.2f}")


print("\n--- Convertir Temperatura de Celsius a Fahrenheit ---")
# Funciones
def celsiusToFahrenheit(celsius):
    return (celsius * 9/5) + 32

# Programa Principal
celsiusValue = utils.leer_decimal_validado("Ingrese la temperatura en Celsius")
fahrenheitValue = celsiusToFahrenheit(celsiusValue)
print(f"{celsiusValue} C equivale a {fahrenheitValue:.2f} F.")


print("\n--- Calcular Promedio de Tres Números ---")
# Funciones
def calculateAverage(num1, num2, num3, cant):
    return (num1 + num2 + num3) / cant

# Programa Principal
num1 = utils.leer_decimal_validado("Ingrese el primer número")
num2 = utils.leer_decimal_validado("Ingrese el segundo número")
num3 = utils.leer_decimal_validado("Ingrese el tercer número")
average = calculateAverage(num1, num2, num3, 3)
print(f"El promedio de {num1} {num2} {num3} es {average:.2f}.")
