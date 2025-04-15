#!/bin/bash
clear

read -p "Ingrese la nota numérica: " nota


while [[ -z "$nota" || "$nota" =~ [^0-9] || "$nota" -lt 0 || "$nota" -gt 10 ]]; do
  echo "Por favor, introduce un número válido (solo números positivos)"
  read -p "Introduce una nota: " nota
done


if [ "$nota" -ge 9 ]; then
  echo "Sobresaliente"
  exit 1
elif [ "$nota" -ge 7 -a "$nota" -lt 9 ]; then
  echo "Notable"
  exit 1
elif [ "$nota" -ge 6 -a "$nota" -lt 7 ]; then
  echo "Bien"
  exit 1
elif [ "$nota" -ge 5 -a "$nota" -lt 6 ]; then
  echo "Suficiente"
  exit 1
elif [ "$nota" -lt 5 ]; then
  echo "Insuficiente"
  exit 1
fi
