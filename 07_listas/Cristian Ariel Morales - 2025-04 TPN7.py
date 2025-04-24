print("Ejercicio 1")
lista = list(range(4, 101, 4))

print(lista)

print("Ejercicio 2")
lista = [1, "hola", True, ["lista", "anidada"], "adios"]

print(lista[3])
print(lista[-2])

print("Ejercicio 3")
lista_vacia = []

lista_vacia.append("hola")
lista_vacia.append("como")
lista_vacia.append("estas")

print(lista_vacia)

print("Ejercicio 4")
animales = ["perro", "gato", "conejo", "pez"]

print(animales)

animales[1] = "loro"
animales[-1] = "oso"

print(animales)

print("Ejercicio 5")
# el ejercicio 5, busca el número máximo de la lista "numeros" y lo elimina

# Creación de la lista
numeros = [8,15,3,22,7]

# remueve el número máximo
numeros.remove(max(numeros))
print(numeros)

print("Ejercicio 6")

list = list(range(10, 31, 5))
print(numeros[:2])

print("Ejercicio 7")
autos = ["sedan", "polo", "suran", "gol"]

autos[1:3] = ["fiesta", "focus"]

print(autos)

print("Ejercicio 8")
dobles = []

dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)

print(dobles)

print("Ejercicio 9")
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],
["agua"]]

compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")

print(compras)

print("Ejercicio 10")
# lista declarada anidada
lista_anidada_declarada = [15, True, [25.5, 57.9, 30.6], False]

#lista vacia declarada
lista_anidada_creada = []

# creación de la lista por posición
lista_anidada_creada.append(15)
lista_anidada_creada.append(True)
lista_anidada_creada.append([25.5, 57.9, 30.6])
lista_anidada_creada.append(False)

print(lista_anidada_declarada)
print(lista_anidada_creada)