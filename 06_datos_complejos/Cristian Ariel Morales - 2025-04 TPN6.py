import math
from collections import deque

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
1450}

precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1700
precios_frutas["Melón"] = 2800

print("Ejercicio 1")
print(precios_frutas)

precios_frutas["Banana"] = 1330
precios_frutas["Manzana"] = 1700
precios_frutas["Melón"] = 2800

print("Ejercicio 2")
print(precios_frutas)


lista_de_keys = list(precios_frutas.keys())

print("Ejercicio 3")
print(lista_de_keys)

class Persona:
    def __init__(self, nombre, pais, edad):
        self.nombre = nombre
        self.pais = pais
        self.edad = edad

    def saludar(nombre, pais, edad):
        print(f"Hola! soy {nombre}, vivo en {pais} y tengo {edad} años.")

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(radio):
        return math.pi * (radio**2)

    def calcular_perimetro(radio):
        return 2 * math.pi * radio


def esta_balanceado(expresion):
    pila = []
    pares = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    for caracter in expresion:
        if caracter in '({[':
            pila.append(caracter)
        elif caracter in ')}]':
            if not pila or pila[-1] != pares[caracter]:
                return False
            pila.pop()

    return not pila 

print("({[]})" , esta_balanceado("({[]})"))    
print("{[()]} ", esta_balanceado("{[()]}"))    
print("{[(])} ", esta_balanceado("{[(])}"))    
print("((())) ", esta_balanceado("((()))"))    
print("({[})" , esta_balanceado("({[})"))     

cola_clientes = deque()

def agregar_cliente(nombre):
    cola_clientes.append(nombre)
    print(f"Cliente '{nombre}' agregado a la cola.")

def atender_cliente():
    if cola_clientes:
        cliente = cola_clientes.popleft()
        print(f"Atendiendo al cliente: {cliente}")
    else:
        print("No hay clientes en la cola.")

def mostrar_siguiente_cliente():
    if cola_clientes:
        print(f"Siguiente cliente en la fila: {cola_clientes[0]}")
    else:
        print("No hay clientes en la fila.")

agregar_cliente("Cristian")
agregar_cliente("Celeste")
agregar_cliente("Ana")

mostrar_siguiente_cliente()  
atender_cliente()            
mostrar_siguiente_cliente()  


class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None 

    def insertar_al_inicio(self, valor):
        nuevo_nodo = Nodo(valor)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def mostrar_lista(self):
        actual = self.cabeza
        while actual:
            print(actual.valor, end=" -> ")
            actual = actual.siguiente
        print("None")

    def invertir(self):
        anterior = None
        actual = self.cabeza
        while actual:
            siguiente = actual.siguiente
            actual.siguiente = anterior
            anterior = actual
            actual = siguiente
        self.cabeza = anterior

lista = ListaEnlazada()
lista.insertar_al_inicio(3)
lista.insertar_al_inicio(2)
lista.insertar_al_inicio(1)

lista.mostrar_lista() 
lista.invertir() 
lista.mostrar_lista() 