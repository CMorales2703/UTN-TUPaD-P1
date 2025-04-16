#!/bin/bash
clear

read -p "¿Cuánto es 2 + 2? " respuesta
intentos=3

# vuelve a realizar la pregunta si la respuesta no es correcta y si los intentos son menores a 1
while [[ "$respuesta" -ne 4 && "$intentos" -lt 1 ]]; do
  intentos=$((intentos - 1))
  echo "Te quedan $intentos intentos."
  read -p "¿Cuánto es 2 + 2? " respuesta
done

# cuando termina el while, si salió porque atino a la respuesta, muestra el correco, sino game over
if [[ "$respuesta" -eq 4 ]]; then
  echo "CORRECTO, acertado en el intento $((4 - intentos))"
else
  echo "Game Over"
fi