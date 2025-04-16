#!/bin/bash
clear

aciertos=0
preguntas=()
respuestas=()

# hacemos un while para recorrer el archivo, usando como delimitador el ;, separando el primer parametro en pregunta y el segundo en respuesta
while IFS=";" read -r pregunta respuesta
do
  # agrego la pregunta y respuesta, a sus listas respectivamente
  preguntas+=("$pregunta")
  respuestas+=("$respuesta")
done < "pregyresp.txt"

# hago un for por el total de los elementos de la lista de preguntas y con el mismo indice la muestro, esperando la respuesta del usuario
for i in "${!preguntas[@]}"; do
  read -p "${preguntas[$i]}? " respuesta

  # si la respuesta del usuario es igual a la respuesta con el mismo indice que la pregunta, incremento aciertos a 1
  if [[ "$respuesta" -eq "${respuestas[$i]}" ]]; then
    aciertos=$((aciertos + 1))
  fi
done

# muestra el total de aciertos obtenidos
echo "Tienes $aciertos aciertos." 