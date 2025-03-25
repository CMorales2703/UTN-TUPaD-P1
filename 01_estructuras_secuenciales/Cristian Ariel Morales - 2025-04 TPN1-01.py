print("Ejercicio 1 - Impresión Hola Mundo")
print("----------------------------------")
print("Hola Mundo!")
print("----------------------------------")
print("")

print("Ejercicio 2 - Saludo")
print("----------------------------------")
name = input("Ingresa tu nombre: ")
print(f"Hola {name}!")
print("----------------------------------")
print("")

print("Ejercicio 3 - Ingreso de datos de usuario")
print("----------------------------------")
name = input("Ingresa tu nombre: ")
lastname = input("Ingresa tu apellido: ")
age = input("Ingresa tu edad: ")
country = input("Ingresa tu país: ")
print(f"Soy {name} {lastname}, tengo {age} años y vivo en {country}")
print("----------------------------------")
print("")

print("Ejercicio 4 - Perimetro de circulo")
print("----------------------------------")
radius = float(input("Ingresa el radio del circulo: "))
pi = 3.14
perimeter = 2 * radius * pi
print(f"El perimetro del circulo con radio de {radius} es de {perimeter}")
print("----------------------------------")
print("")

print("Ejercicio 5 - Segundos a Hora")
print("----------------------------------")
seconds = int(input("Ingresa una cantidad de segundos: "))
hour = 3600
secondsToHours = seconds / hour
if secondsToHours == 1:
    print(f"{seconds} segundos es {int(secondsToHours)} hora")
else:   
    print(f"{seconds} segundos son {secondsToHours:.2f} horas")
print("----------------------------------")
print("")

print("Ejercicio 6 - Tabla de multiplicación")
print("----------------------------------")
num = float(input("Ingresa el número que desea multiplicar: "))
multiple = int(input("Ingresa hasta que número quiere multiplicar (solo enteros): "))
for i in range(1, multiple + 1):
    print(f"{num} X {i} = {num * i}")
print("----------------------------------")
print("")

print("Ejercicio 7 - Operaciones  aritméticas con dos números distintos de 0")
print("----------------------------------")
while True:
    firstNum = int(input("Ingresa el primer número distinto de cero: "))

    if firstNum != 0:
        break

while True:
    secondName = int(input("Ingresa el segundo número distinto de cero: "))

    if secondName != 0:
        break

print(f"{firstNum} sumado por {secondName} es igual a {firstNum + secondName}")
print(f"{firstNum} restado por {secondName} es igual a {firstNum - secondName}")
print(f"{firstNum} multiplicado por {secondName} es igual a {firstNum * secondName}")
print(f"{firstNum} dividio por {secondName} es igual a {firstNum / secondName}")
print("----------------------------------")
print("")

print("Ejercicio 8 - Indice de masa corporal (IMC)")
print("----------------------------------")
while True:
    height = float(input("Ingresa su altura en metros: "))

    if height > 0:
        break

while True:
    weight = float(input("Ingresa su peso en KG: "))

    if weight > 0:
        break
imc = weight / (height ** 2)

print(f"Tu IMC es {imc:.2f}")
print("----------------------------------")
print("")

print("Ejercicio 9 - Conversión Celsius a Fahrenheit")
print("----------------------------------")
temperatureC = float(input("Ingresa la temperatura en Celsius: "))
temperatureF = (9/5) * temperatureC + 32
print(f"{temperatureC} °C son {temperatureF} °F")
print("----------------------------------")
print("")

print("Ejercicio 10 - Promedio de 3 números")
print("----------------------------------")
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
num3 = float(input("Ingresa el tercer número: "))
average = (num1 + num2 + num3) / 3
print(f"El promedio de {num1}, {num2} y {num3} es de {average}")
print("----------------------------------")
print("")
