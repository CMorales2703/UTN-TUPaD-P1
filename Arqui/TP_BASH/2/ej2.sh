#!/bin/bash
clear

# imprime el menu de opciones
echo "Opciones:"
echo "1. Calcular el área de un rectángulo."  
echo "2. Calcular el perímetro de un rectángulo."
echo "3. Salir"
read -p "Seleccione una opción (1-3): " opcion

# valida que la opcion sea 1 2 o 3
while [[ -z "$opcion" || ! "$opcion" =~ ^[1-3]$ ]]; do
  echo "Por favor, introduce la opción correcta: "
  read -p "Seleccione una opción (1-3): " opcion
done

case $opcion in
  1)
    # si la opcion es 1, pide el ingreso de datos para calcular el area
    read -p "Ingrese la base del rectángulo: " base

    # valida que sea un número positivo
    while [[ -z "$base" || ! "$base" =~ ^[0-9]+([.][0-9]+)?$ ]]; do
      echo "Por favor, introduce un número válido: "
      read -p "Ingrese la base del rectángulo: " base
    done

    # valida que sea un número positivo
    read -p "Ingrese la altura del rectángulo: " altura
    while [[ -z "$altura" || ! "$base" =~ ^[0-9]+([.][0-9]+)?$ ]]; do
      echo "Por favor, introduce un número válido: "
      read -p "Ingrese la altura del rectángulo: " altura
    done

    # calcula el area
    area=$(echo "$base * $altura" | bc)
    echo "El área del rectángulo es: $area"
    ;;
  2)
    # si la opcion es 2, pide el ingreso de datos para calcular el perimetro
    read -p "Ingrese la base del rectángulo: " base

    # valida que sea un número positivo
    while [[ -z "$base" || ! "$base" =~ ^[0-9]+([.][0-9]+)?$ ]]; do
      echo "Por favor, introduce un número válido: "
      read -p "Ingrese la base del rectángulo: " base
    done
    read -p "Ingrese la altura del rectángulo: " altura

    # valida que sea un número positivo
    while [[ -z "$altura" || ! "$base" =~ ^[0-9]+([.][0-9]+)?$ ]]; do
      echo "Por favor, introduce un número válido: "
      read -p "Ingrese la altura del rectángulo: " altura
    done
    perimetro=$(echo "2 * ($base + $altura)" | bc)
    echo "El perímetro del rectángulo es: $perimetro"
    ;;
  3)
    # opcion 3 termina el programa
    echo "Saliendo..."
    exit 0
    ;;
esac