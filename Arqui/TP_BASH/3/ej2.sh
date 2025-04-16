#!/bin/bash
clear

read -p "Extensión del archivo: " extension

for archivo in *."$extension"; do
  if [[ -e "$archivo" ]]; then
    echo "Nombre del archivo: $archivo"
    echo "=================================="
    cat "$archivo"
    echo ""
    echo "=================================="
  else
    echo "No se encuentran archivos con esa extensión"
    exit 1
  fi
done