#!/bin/bash

clear
# importo el script script20_gestion.sh
source script20_gestion.sh

# función de menú principal
function menu_principal(){
    echo "" 
    # imprime opciones del menú
    echo "Menú Principal"
    echo "1. Información de usuario"
    echo "2. Gestión de usuario"
    echo "3. Salir"
    read -p "Elige una opción: " opcion

    # llamada a la función para validar la opción ingresada (1, 2 o 3)
    respuesta=$(validar_opcion $opcion "^[1-3]$" "(1,2,3)")

    # ejecuta la acción correspondiente
    case $respuesta in 
        # muestra información del usuario
        1) Informacion_usuario ;;    
        # abre el menú de gestión
        2) gestion_de_usuarios ;;    
        # sale del programa
        3) exit ;;                   
    esac
}

# bucle del menú principal hasta que se elija salir (opción 3)
while true; do
    menu_principal  
done
