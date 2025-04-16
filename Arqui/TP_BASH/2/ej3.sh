#!/bin/bash
clear
echo "Carga de números, el 999 termina la carga"  

# crea una lista
numeros=()

# peticion y validacion de número
read -p "Ingrese un número: " numero
while [[ -z "$numero" || ! "$numero" =~ ^[0-9]+([.][0-9]+)?$ ]]; do
  echo "Por favor, introduce un número válido: "
  read -p "Ingrese un número: " numero
done

# realiza un while mientras el número ingresado sea diferente de 999
while [[ ! "$numero" =~ 999 ]]; do

  # por cada número, se ingresa a la lista
  numeros+=("$numero")

  # peticion y validacion de número
  read -p "Siguiente un número: " numero
  while [[ -z "$numero" || ! "$numero" =~ ^[0-9]+([.][0-9]+)?$ ]]; do
    echo "Por favor, introduce un número válido: "
    read -p "Siguiente un número: " numero
  done
done

# peticion para ver los números
read -p "¿Quieres ver los números introducidos?(s/n)" opcion

# validación de opción
while [[ ! "$opcion" =~ ^[n,N,s,S]$ ]]; do
  echo "Por favor, introduce una opción válida (s/n): "
  read -p "¿Quieres ver los números introducidos?(s/n)" opcion
done

# peticion para ordenar los números
if [[ "$opcion" =~ s ]]; then 
  read -p "¿Orden de ingreso, ascendente o descendente?(o/a/d)" orden

  # validación de opción
  while [[ ! "$orden" =~ ^[o,O,a,A,d,D]$ ]]; do
    echo "Por favor, introduce una opción válida (O/A/D): "
    read -p "¿Orden de ingreso, ascendente o descendente?(o/a/d)" orden
  done

  # impresión del orden seleccionado
  if [[ "$orden" =~ ^[o,O]$ ]]; then
    echo "Orden de ingreso"
    echo "${numeros[@]}"
  elif [[ "$orden" =~ ^[a,A]$ ]]; then
    echo "Orden ascendente"
    echo "${numeros[@]}" | tr ' ' '\n' | sort -n
  elif [[ "$orden" =~ ^[d,D]$ ]]; then
    echo "Orden descendente"
    echo "${numeros[@]}" | tr ' ' '\n' | sort -nr
  fi
else
  echo "Hasta la vista"
fi
