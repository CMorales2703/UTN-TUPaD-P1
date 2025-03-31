print("Verificación de mayoría de edad")
MIN_AGE = 18
age = int(input("Ingrese su edad: "))
if age > MIN_AGE:
    print("Es mayor de edad")

print("Verificación de nota aprobatoria")
MIN_NOTE = 6
note = int(input("Ingrese su nota: "))
if note >= MIN_NOTE:
    print("Aprobado")
else:
    print("Desaprobado")

print("Verificación de número par")
num = int(input("Ingrese un número: "))
if num % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

print("Clasificación por edad")
age = int(input("Ingrese su edad: "))
if age < 12:
    print("Niño/a")
elif age >= 12 and age < 18:
    print("Adolescente")
elif age >= 18 and age < 30:
    print("Adulto/a joven")
elif age >= 30:
    print("Adulto/a")


print("Validación de longitud de contraseña")
PASS_MIN = 8
PASS_MAX = 14
password = input(f"Ingrese su contraseña (entre {PASS_MIN} y {PASS_MAX} caracteres inclusives): ")

if len(password) >= PASS_MIN and len(password) <= PASS_MAX:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")


print("Cálculo de moda, mediana y media en una lista aleatoria")
from statistics import mode, median, mean
import random

randomListNumbers = [random.randint(1, 100) for i in range(50)]

moda = mode(randomListNumbers)
mediana = median(randomListNumbers)
media = mean(randomListNumbers)

# Imprimir los resultados
print(f"Moda: {moda}")
print(f"Mediana: {mediana}")
print(f"Media: {media}")

if media > mediana > moda:
    print("Sesgo positivo o a la derecha")
elif media < mediana < moda:
    print("Sesgo negativo o a la izquierda")
else:
    print("Sin sesgo")

print("Formato de nombre según opción del usuario")
name = input("Ingrese su nombre: ")
print("Ingrese la opción deseada (solo el número):")
print("1 - Nombre en mayúsculas")
print("2 - Nombre en minúsculas:")
print("3 - Nombre con la primera letra mayúscula")
option = int(input())

if option == 1:
    print(f"{name.upper()}")
elif option == 2:
    print(f"{name.lower()}")
elif option == 3:
    print(f"{name.title()}")


print("Clasificación de magnitud de terremotos")
magnitude = int(input("Ingrese la magnitud del terremoto: "))

if magnitude < 3:
    print("Muy leve (imperceptible)")
elif magnitude >= 3 and magnitude < 4:
    print("Leve (ligeramente perceptible)")
elif magnitude >= 4 and magnitude < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitude >= 5 and magnitude < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif magnitude >= 6 and magnitude < 7:
    print("Muy Fuerte (puede causar daños significativos)")
elif magnitude >= 7:
    print("Extremo (puede causar graves daños a gran escala)")

print("Determinación de estación del año según fecha y hemisferio")
hemisphere = input("Ingrese el hemisferio donde se encuentra (N/S): ").upper()
month = int(input("En que Mes estas? (1-12): "))
day = int(input("En que dia estas? (1-31): "))

if month < 1 or month > 12 or day < 1 or day > 31:
    print("Fecha no válida.")
else:
    if hemisphere == 'N': 
        if (month == 12 and day >= 21) or (month <= 3 and day <= 20):
            season = "Invierno"
        elif (month == 3 and day >= 21) or (month <= 6 and day <= 20):
            season = "Primavera"
        elif (month == 6 and day >= 21) or (month <= 9 and day <= 20):
            season = "Verano"
        elif (month == 9 and day >= 21) or (month <= 12 and day <= 20):
            season = "Otoño"
    
    elif hemisphere == 'S': 
        if (month == 12 and day >= 21) or (month <= 3 and day <= 20):
            season = "Verano"
        elif (month == 3 and day >= 21) or (month <= 6 and day <= 20):
            season = "Otoño"
        elif (month == 6 and day >= 21) or (month <= 9 and day <= 20):
            season = "Invierno"
        elif (month == 9 and day >= 21) or (month <= 12 and day <= 20):
            season = "Primavera"
    else:
        season = "Hemisferio no válido"
    
    print(f"La estación es: {season}")
