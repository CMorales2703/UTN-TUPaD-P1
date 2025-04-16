#!/bin/bash

clear
source script20_gestion.sh

function menu_principal(){
    echo "" 
    echo "Menú Principal"
    echo "1. Información de usuario"
    echo "2. Gestión de usuario"
    echo "3. Salir"
    read -p "Elige una opción: " opcion

    respuesta=$(validar_opcion $opcion "^[1-3]$" "(1,2,3)")
    case $respuesta in 
        1) Informacion_usuario ;; 
        2) gestion_de_usuarios ;; 
        3) exit ;; 
    esac
}

while true; do
    menu_principal  
done
