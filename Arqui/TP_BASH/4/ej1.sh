#!/bin/bash
clear

archivo_final="union.txt"
touch $archivo_final

while IFS="," read -r equipo estadio
do
  equipo=$(echo "$equipo" | xargs)
  while IFS=";" read -r colores equipo2
  do
    equipo2=$(echo "$equipo2" | xargs) 
    if [[ "$equipo" == "$equipo2" ]]; then
      echo "$equipo;$colores;$estadio" >> $archivo_final
    fi
  done < "arch2.txt"
done < "arch1.txt"