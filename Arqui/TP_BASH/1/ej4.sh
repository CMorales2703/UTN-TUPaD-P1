#!/bin/bash
clear

# pide ingreso de una cadena y verifica si esta vacía
read -p "Ingrese una cadena: " cadena1
if [ -z "$cadena1" ]; then
  echo "La cadena1 está vacía"
else
    echo "La cadena1 no está vacía"
fi

read -p "Ingrese otra cadena: " cadena2
if [ -z "$cadena2" ]; then
  echo "La cadena2 está vacía"
else
    echo "La cadena2 no está vacía"
fi

# compara ambas cadenas si son iguales o no
if [ "$cadena1" == "$cadena2" ]; then
  echo "Las cadenas son iguales"
else
    echo "Las cadenas son diferentes"
fi