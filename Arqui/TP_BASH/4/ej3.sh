#!/bin/bash
puntuacion="puntuacion.txt"
clear

# verifica que el último bit del archivo si tiene dato, si es asi, agrega un salto de página
if [[ $(tail -c 1 $puntuacion | od -An -t x1 | xargs) != "0a" ]]; then
    echo >> $puntuacion
fi

pilotos=()
puntajes=()

# recorro el archivo puntuacion.txt, delimitando cada lina por , separando el primer dato como piloto y el segundo como puntos_acumulados
while IFS="," read -r piloto puntos_acumulados
do
    # elimino posibles espacios
    piloto=$(echo "$piloto" | xargs)
    puntos_acumulados=$(echo "$puntos_acumulados" | xargs)

    # agrego los pilotos y los puntos_acumulados a cada lista correspondiente
    pilotos+=("$piloto")
    puntajes+=("$puntos_acumulados")

done < $puntuacion

# recorro la lista de pilotos
for i in "${!pilotos[@]}"; do
    # por cada indice, tomo el piloto, pido el putaje nuevo
    read -p "Puntaje ${pilotos[$i]}? " puntaje
    # elimino la linea del piloto en el archivo
    sed -i "/^${pilotos[$i]},/d" $puntuacion
    # ingreso neuvamente el piloto con la suma de los puntos_acumulados y el nuevo puntaje al archivo puntuacion
    echo "${pilotos[$i]},$((${puntajes[$i]} + $puntaje))" >> $puntuacion
done

# ordena de forma descendente por número y lo modifica en el archivo
sort -t',' -k2 -nr "$puntuacion" -o "$puntuacion"