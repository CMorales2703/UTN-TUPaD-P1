#!/bin/bash
clear
echo "Carga de números, el 999 termina la carga"  

numeros=()

read -p "Ingrese un número: " numero
while [[ -z "$numero" || ! "$numero" =~ ^[0-9]+([.][0-9]+)?$ ]]; do
  echo "Por favor, introduce un número válido: "
  read -p "Ingrese un número: " numero
done


while [[ ! "$numero" =~ 999 ]]; do
  numeros+=("$numero")
  read -p "Siguiente un número: " numero
  while [[ -z "$numero" || ! "$numero" =~ ^[0-9]+([.][0-9]+)?$ ]]; do
    echo "Por favor, introduce un número válido: "
    read -p "Siguiente un número: " numero
  done
done

read -p "¿Quieres ver los números introducidos?(s/n)" opcion

while [[ ! "$opcion" =~ ^[n,N,s,S]$ ]]; do
  echo "Por favor, introduce una opción válida (s/n): "
  read -p "¿Quieres ver los números introducidos?(s/n)" opcion
done

if [[ "$opcion" =~ s ]]; then 
  read -p "¿Orden de ingreso, ascendente o descendente?(o/a/d)" orden
  while [[ ! "$orden" =~ ^[o,O,a,A,d,D]$ ]]; do
    echo "Por favor, introduce una opción válida (O/A/D): "
    read -p "¿Orden de ingreso, ascendente o descendente?(o/a/d)" orden
  done

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
