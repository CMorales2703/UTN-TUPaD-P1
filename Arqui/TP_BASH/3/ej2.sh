#!/bin/bash
clear

read -p "Extensión del archivo: " extension

# se realiza un for de todos los archivos con la extensión solicitada
for archivo in *."$extension"; do
  # si existe, se muestra el nombre y el contenido del mismo
  if [[ -e "$archivo" ]]; then
    echo "Nombre del archivo: $archivo"
    echo "=================================="
    cat "$archivo"
    echo ""
    echo "=================================="
  else
    # caso contrario, imprime que no se encuentran archivos con esa extensión y se termina el bucle
    echo "No se encuentran archivos con esa extensión"
    exit 1
  fi
done