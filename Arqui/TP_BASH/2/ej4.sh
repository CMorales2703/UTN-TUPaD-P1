#!/bin/bash
clear

read -p "¿Cuánto es 2 + 2? " respuesta
intentos=3
while [[ "$respuesta" -ne 4 && "$intentos" -lt 1 ]]; do
  intentos=$((intentos - 1))
  echo "Te quedan $intentos intentos."
  read -p "¿Cuánto es 2 + 2? " respuesta
done

if [[ "$respuesta" -eq 4 ]]; then
  echo "CORRECTO, acertado en el intento $((4 - intentos))"
else
  echo "Game Over"
fi