#!/bin/bash
puntuacion="puntuacion.txt"
puntuacionTemp="puntuacion.temp"

rm $puntuacionTemp
touch $puntuacionTemp

pilotos=()
puntajes=()

clear

function ordenar_y_mostrar(){
    echo ""
    sort -t',' -k2 -nr "$puntuacion" -o "$puntuacion"
    cat $puntuacion;
}

function agregar_salto_linea(){
    if [[ $(tail -c 1 $puntuacion | od -An -t x1 | xargs) != "0a" ]]; then
        echo >> $puntuacion
    fi
}
function lee_jugador_y_puntos() {
    local numero_linea=$1
    IFS="," read -r piloto puntos_acumulados <<< $(sed -n "${numero_linea}p" "$puntuacion")
    echo "$piloto,$puntos_acumulados"
}

function actualizar_puntos(){
    local piloto=$1
    local puntos=$2
    local puntos_antiguos=$3

    echo "$piloto,$((puntos + puntos_antiguos))" >> $puntuacionTemp
}

function procesar_puntuaciones() {
    agregar_salto_linea
    
    lineas_totales=$(wc -l < $puntuacion)

    for ((i=1; i<=lineas_totales; i++)); do
        datos_piloto=$(lee_jugador_y_puntos $i)
    
        piloto=$(echo $datos_piloto | cut -d',' -f1)
        puntos_acumulados=$(echo $datos_piloto | cut -d',' -f2)
        read -p "Puntos de $piloto: " puntos

        actualizar_puntos $piloto $puntos_acumulados $puntos
    done
    cp "$puntuacionTemp" "$puntuacion"
    ordenar_y_mostrar
    rm $puntuacionTemp
}


procesar_puntuaciones