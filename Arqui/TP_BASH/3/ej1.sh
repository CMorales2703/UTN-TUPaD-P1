#!/bin/bash
clear

read -p "Ingrese la ruta del archivo: " ruta

# verifica si esa ruta archivo/directorio, existe
if [[ -e "$ruta" ]]; then
  echo ""
  echo "Archivo: $ruta"
  echo ""
  echo "El archivo $ruta existe"
  echo ""

  # imprime que tipo de archivo es o si es un directorio
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
  # verifica si es un archivo ordinario o directorio, para evitar los archivos especiales
  if [[ -f "$ruta" || -d "$ruta" ]]; then
  # imprime si ese archivo/directorio tiene permisos de lectura, escritura y/o ejecución
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
    # en caso de ser un archivo especial, no se muestran los permisos
    echo "No se muestran permisos para archivos especiales."
  fi

else
  # si la ruta no existe, se muestra por pantalla la leyenda que no existe
  echo "El archivo/directorio no existe"
fi