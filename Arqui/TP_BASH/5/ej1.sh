#!/bin/bash
puntuacion="puntuacion.txt"
puntuacionTemp="puntuacion.temp"

# elimino y creo el archivo temp
rm $puntuacionTemp
touch $puntuacionTemp

pilotos=()
puntajes=()

clear

# función para ordenar y mostrar las puntuaciones de forma descendentes numericamente
function ordenar_y_mostrar(){
    echo ""
    sort -t',' -k2 -nr "$puntuacion" -o "$puntuacion"
    cat $puntuacion;
}

# función para agregar salto de linea
function agregar_salto_linea(){
    if [[ $(tail -c 1 $puntuacion | od -An -t x1 | xargs) != "0a" ]]; then
        echo >> $puntuacion
    fi
}

# función para leer el piloto y sus puntos del archivo puntuacion, indicando el número de linea
function lee_jugador_y_puntos() {
    local numero_linea=$1
    IFS="," read -r piloto puntos_acumulados <<< $(sed -n "${numero_linea}p" "$puntuacion")
    echo "$piloto,$puntos_acumulados"
}

# ingresa los datos actualizados del piloto con su puntuacion antigua y la nueva al archivo temp
function actualizar_puntos(){
    local piloto=$1
    local puntos=$2
    local puntos_antiguos=$3

    echo "$piloto,$((puntos + puntos_antiguos))" >> $puntuacionTemp
}

# función de programa principal
function procesar_puntuaciones() {
    # llamada a la función
    agregar_salto_linea
    
    # indica las lineas totales del archivo puntuación
    lineas_totales=$(wc -l < $puntuacion)

    # realizo un for desde 1 hasta la cantidad total de lineas de archivos
    for ((i=1; i<=lineas_totales; i++)); do
        # leo los datos del piloto usando el indice i como numero de pagina
        datos_piloto=$(lee_jugador_y_puntos $i)

        # separo el primer campo (nombre del piloto) de la línea "datos_piloto", separada por comas
        piloto=$(echo $datos_piloto | cut -d',' -f1)

        # separo el segundo campo (puntos acumulados) de la línea "datos_piloto", separada por comas
        puntos_acumulados=$(echo $datos_piloto | cut -d',' -f2)

        # pido al usuario los nuevos puntos
        read -p "Puntos de $piloto: " puntos

        # llamada a la función con los parametros necesarios
        actualizar_puntos $piloto $puntos_acumulados $puntos
    done
    # copia de contenido de temp a puntuacion
    cp "$puntuacionTemp" "$puntuacion"
    # llamada a la función
    ordenar_y_mostrar

    # eliminar archivo temp
    rm $puntuacionTemp
}

# llamada del programa principal 
procesar_puntuaciones