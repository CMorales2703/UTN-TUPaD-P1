# Programa 1: Imprimir números del 0 al 100
print("==== Programa 1: Imprimir números del 0 al 100 ====")
for i in range(100+1):
    print(i)

# Programa 2: Contar dígitos de un número
print("\n==== Programa 2: Contar dígitos de un número ====")
num = int(input("Ingrese un número: "))
digitQuantity = len(str(abs(num)))
print(f"El número tiene {digitQuantity} dígitos.")

# Programa 3: Sumar números entre dos valores (sin incluirlos)
print("\n==== Programa 3: Sumar números entre dos valores (sin incluirlos) ====")
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
total = 0

if num1 < num2:
    for i in range(num1 + 1, num2):
        total += i
    print(f"La suma entre {num1} y {num2} (sin incluirse) es de {total}.")
elif num1 > num2:
    for i in range(num2 + 1, num1):
        total += i
    print(f"La suma entre {num2} y {num1} (sin incluirse) es de {total}.")
else:
    print(f"La suma entre {num1} y {num2} (sin incluirse) es de {total}.")

# Programa 4: Sumar números hasta que se ingrese 0
print("\n==== Programa 4: Sumar números hasta que se ingrese 0 ====")
print("Para salir, ingrese 0")
total = 0
num = int(input("Ingrese un número entero: "))

while num != 0:
    total += num
    num = int(input("Ingrese un número entero: "))

print(f"La suma total es de {total}")

# Programa 5: Juego de adivinar el número
print("\n==== Programa 5: Juego de adivinar el número ====")
import random
randomNumber = random.randint(0, 9)
guessTrys = 0

print("Adivina el número, entre el 0 y el 9")
num = int(input("Ingresa tu número: "))
guessTrys += 1

while num != randomNumber:
    print("Incorrecto. Intenta de nuevo.")
    num = int(input("Ingresa tu número: "))
    guessTrys += 1

print(f"Felicitaciones!")
if guessTrys > 1:
    print(f"Adivinaste el número en {guessTrys} intentos.")
else:
    print(f"Adivinaste el número en {guessTrys} intento.")

# Programa 6: Imprimir números pares de 2 a 100 en orden descendente
print("\n==== Programa 6: Imprimir números pares de 2 a 100 en orden descendente ====")
for i in reversed(range(2, 100, 2)):
    print(i)

# Programa 7: Sumar números de 0 a N (sin incluir N)
print("\n==== Programa 7: Sumar números de 0 a N (sin incluir N) ====")
num = abs(int(input("Ingrese un número entero positivo: ")))
total = 0

for i in range(0, num):
    total += i
print(f"El total de 0 a {num} es de {total}")

# Programa 8: Contar positivos, negativos, pares e impares
print("\n==== Programa 8: Contar positivos, negativos, pares e impares ====")
QUANTITY_NUMBERS = 100

quantityNeg = 0
quantityPos = 0
quantityImp = 0
quantityPair = 0

for i in range(QUANTITY_NUMBERS):
    num = int(input("Ingresa un número entero: "))
    if num % 2 == 0:
        quantityPair += 1
    else:
        quantityImp += 1

    if num > 0:
        quantityPos += 1
    elif num < 0:
        quantityNeg += 1

print(f"Números Pares: {quantityPair}")
print(f"Números Impares: {quantityImp}")
print(f"Números Positivos: {quantityPos}")
print(f"Números Negativos: {quantityNeg}")

# Programa 9: Calcular la media
print("\n==== Programa 9: Calcular la media ====")
QUANTITY_NUMBERS = 100
total = 0

for i in range(QUANTITY_NUMBERS):
    num = int(input("Ingresa un número entero: "))
    total += num

print(f"La media es de: {total} {total / QUANTITY_NUMBERS}")

# Programa 10: Invertir un número
print("\n==== Programa 10: Invertir un número ====")
num = abs(int(input("Ingrese un número: ")))
numInverted = str(num)[::-1]
print(f"El número invertido es {numInverted}")
