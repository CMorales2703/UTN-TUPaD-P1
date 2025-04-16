#!/bin/bash
puntuacion="puntuacion.txt"
clear

if [[ $(tail -c 1 $puntuacion | od -An -t x1 | xargs) != "0a" ]]; then
    echo >> $puntuacion
fi

pilotos=()
puntajes=()

while IFS="," read -r piloto puntos_acumulados
do
    piloto=$(echo "$piloto" | xargs)
    puntos_acumulados=$(echo "$puntos_acumulados" | xargs)

    pilotos+=("$piloto")
    puntajes+=("$puntos_acumulados")

done < $puntuacion

for i in "${!pilotos[@]}"; do
    read -p "Puntaje ${pilotos[$i]}? " puntaje
    sed -i "/^${pilotos[$i]},/d" $puntuacion
    echo "${pilotos[$i]},$((${puntajes[$i]} + $puntaje))" >> $puntuacion
done

sort -t',' -k2 -nr "$puntuacion" -o "$puntuacion"