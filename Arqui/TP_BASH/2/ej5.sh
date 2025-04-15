#!/bin/bash
clear

aciertos=0
preguntas=()
respuestas=()

while IFS=";" read -r pregunta respuesta
do
  preguntas+=("$pregunta")
  respuestas+=("$respuesta")
done < "pregyresp.txt"

for i in "${!preguntas[@]}"; do
  read -p "${preguntas[$i]}? " respuesta

  if [[ "$respuesta" -eq "${respuestas[$i]}" ]]; then
    aciertos=$((aciertos + 1))
  fi
done

echo "Tienes $aciertos aciertos."