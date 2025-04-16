#!/bin/bash
clear

num1=$1
num2=$2

# verifica si no se introdujo ningún parámetro y los pide
if [ "$#" == 0 ]; then
  read -p "No ha introducido ninguno. ¿Quiere ahora s/n?" respuesta

  # si pone que si, se piden ambos números
  if [ "$respuesta" == "s" ]; then
    read -p "Ingrese el primer número: " num1
    read -p "Ingrese el segundo número: " num2
  else
  # si pone que no, sale de la aplicación
    echo "Saliendo..."
    exit 1
  fi

  # verifica si no se introdujo 1 parámetro y pide el 2
  elif [ "$#" == 1 ]; then
  read -p "Ha introducido uno. ¿Quiere ahora s/n?" respuesta

  # si pone que si, se piden el número faltante
  if [ "$respuesta" == "s" ]; then
    read -p "Ingrese el segundo número: " num2
  else
   # si pone que no, sale de la aplicación
    echo "Saliendo..."
    exit 1
  fi

  # verifica si hay mas de 2 parámetros, en tal caso, toma los dos primeros
  elif [ "$#" -gt 2 ]; then 
    echo "Demasiados parámetros, tomo los dos primeros."
    num1=$1
    num2=$2

  # verifica si hay 2 parámetros y asigna los parámetros a sus respctivas variables
  elif [ "$#" == 2 ]; then
    echo "CORRECTO"
    num1=$1
    num2=$2
fi

# imprime las cuentas aritméticas entre ambos números
echo "Suma: $(($num1 + $num2))"
echo "Resta: $(($num1 - $num2))"
echo "Multiplicación: $(($num1 * $num2))"

# si num2 es 0, muestra un mensaje que no se puede dividir por 0
if [ $num2 -eq 0 ]; then
  echo "No se puede dividir por cero"
else
  echo "División: $(($num1 / $num2))"
fi

