#!/bin/bash
clear

archivo_final="union.txt"
# creo el archivo final (union.txt)
touch $archivo_final

# recorro el archivo arch1.txt, delimitando cada lina por , separando el primer dato como equipo y el segundo como estadio
while IFS="," read -r equipo estadio
do
  # por cada valor, uso xargs para eliminar posibles espacios y lo vuelvo a asignar
  equipo=$(echo "$equipo" | xargs)

  # recorro el archivo arch2.txt, delimitando cada lina por ; separando el primer dato como colores y el segundo como equipo_colores
  while IFS=";" read -r colores equipo_colores
  do
    equipo_colores=$(echo "$equipo_colores" | xargs) 

    # comparo si equipo y equipo_colores es lo mismo, si se cumple la condición, armo la estructura de datos con equipo, colores y estadio y la agrego a archivo_final
    if [[ "$equipo" == "$equipo_colores" ]]; then
      echo "$equipo;$colores;$estadio" >> $archivo_final
    fi
  done < "arch2.txt"
done < "arch1.txt"