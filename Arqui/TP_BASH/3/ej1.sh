#!/bin/bash
clear

read -p "Ingrese la ruta del archivo: " ruta

if [[ -e "$ruta" ]]; then
  echo ""
  echo "Archivo: $ruta"
  echo ""
  echo "El archivo $ruta existe"
  echo ""

  if [[ -b "$ruta" ]]; then
    echo "Es un archivo especial de bloques"
  elif [[ -c "$ruta" ]]; then
    echo "Es un archivo de caracteres"
  elif [[ -d "$ruta" ]]; then
    echo "Es un directorio"
  elif [[ -f "$ruta" ]]; then
    echo "Es un archivo ordinario"
  elif [[ -h "$ruta" ]]; then
    echo "Es un archivo simbólico"
  fi

  echo ""
  if [[ -f "$ruta" || -d "$ruta" ]]; then
    if [[ -r "$ruta" ]]; then
      echo "Tiene permiso de lectura"
      echo ""
    fi
    if [[ -w "$ruta" ]]; then
      echo "Tiene permiso de escritura"
      echo ""
    fi
    if [[ -x "$ruta" ]]; then
      echo "Tiene permiso de ejecución"
      echo ""
    fi
  else
    echo "No se muestran permisos para archivos especiales."
  fi

else
  echo "El archivo no existe"
fi