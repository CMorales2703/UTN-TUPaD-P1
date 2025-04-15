#!/bin/bash
clear
echo "Opciones:"
echo "1. Calcular el área de un rectángulo."  
echo "2. Calcular el perímetro de un rectángulo."
echo "3. Salir"
echo "Seleccione una opción (1-3):"
read -p "Opción: " opcion
while [[ -z "$opcion" || "$opcion" =~ [^0-9] || ! "$opcion" =~ ^[1-3]$ ]]; do
  echo "Por favor, introduce la opción correcta: "
  read -p "Seleccione una opción (1-3): " opcion
done

case $opcion in
  1)
    read -p "Ingrese la base del rectángulo: " base
    while [[ -z "$base" || ! "$base" =~ ^[0-9]+([.][0-9]+)?$ ]]; do
      echo "Por favor, introduce un número válido: "
      read -p "Ingrese la base del rectángulo: " base
    done

    read -p "Ingrese la altura del rectángulo: " altura
    while [[ -z "$altura" || ! "$base" =~ ^[0-9]+([.][0-9]+)?$ ]]; do
      echo "Por favor, introduce un número válido: "
      read -p "Ingrese la altura del rectángulo: " altura
    done

    area=$(echo "$base * $altura" | bc)
    echo "El área del rectángulo es: $area"
    ;;
  2)
    read -p "Ingrese la base del rectángulo: " base
    while [[ -z "$base" || ! "$base" =~ ^[0-9]+([.][0-9]+)?$ ]]; do
      echo "Por favor, introduce un número válido: "
      read -p "Ingrese la base del rectángulo: " base
    done
    read -p "Ingrese la altura del rectángulo: " altura

    while [[ -z "$altura" || ! "$base" =~ ^[0-9]+([.][0-9]+)?$ ]]; do
      echo "Por favor, introduce un número válido: "
      read -p "Ingrese la altura del rectángulo: " altura
    done
    perimetro=$(echo "2 * ($base + $altura)" | bc)
    echo "El perímetro del rectángulo es: $perimetro"
    ;;
  3)
    echo "Saliendo..."
    exit 0
    ;;
esac