#!/bin/bash
clear

num1=$1
num2=$2

if [ "$#" == 0 ]; then
  read -p "No ha introducido ninguno. ¿Quiere ahora s/n?" respuesta
  if [ "$respuesta" == "s" ]; then
    read -p "Ingrese el primer número: " num1
    read -p "Ingrese el segundo número: " num2
  else
    echo "Saliendo..."
    exit 1
  fi
  elif [ "$#" == 1 ]; then
  read -p "Ha introducido uno. ¿Quiere ahora s/n?" respuesta
  if [ "$respuesta" == "s" ]; then
    read -p "Ingrese el segundo número: " num2
  else
    echo "Saliendo..."
    exit 1
  fi
  elif [ "$#" -gt 2 ]; then 
  echo "Demasiados parámetros, tomo los dos primeros."
  num1=$1
  num2=$2
  elif [ "$#" == 2 ]; then
  echo "CORRECTO"
  num1=$1
  num2=$2
fi

echo "Suma: $(($num1 + $num2))"
echo "Resta: $(($num1 - $num2))"
echo "Multiplicación: $(($num1 * $num2))"
if [ $num2 -eq 0 ]; then
  echo "No se puede dividir por cero"
else
  echo "División: $(($num1 / $num2))"
fi

