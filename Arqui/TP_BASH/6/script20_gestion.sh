#!/bin/bash


function Informacion_usuario(){
    read -p "Ingrese el nombre del usuario: " usuario

    if existe_usuario "$usuario"; then
        echo "El usuario no existe"
    else
        echo "Usuario encontrado"
        finger "$usuario"
    fi
}

function existe_usuario(){
    local usuario=$1
    if ! id "$usuario" &>/dev/null; then
        return 0  
    else
        return 1  
    fi
}

function validar_opcion(){ 
    local opcion=$1
    local criterios=$2
    local opciones=$3

    while [[ ! "$opcion" =~ $criterios ]]; do
        read -p "Por favor, introduce una opción válida $opciones: " opcion
    done
    echo "${opcion^^}"
}

function agregar_usuario(){
    if groups "$USER" | grep -q '\bsudo\b'; then
        read -p "Nombre del usuario: " nuevo_usuario

        if existe_usuario "$nuevo_usuario"; then
            echo "El usuario no existe." 
            if sudo adduser "$nuevo_usuario"; then
                echo "Usuario $nuevo_usuario creado correctamente."
            else
                echo "Error al crear usuario."
            fi
        else
            echo "El usuario ya existe."
        fi
    else
        echo "No tiene permiso de administrador."  
    fi
}

function eliminar_usuario(){
    if groups "$USER" | grep -q '\bsudo\b'; then
        read -p "Nombre del usuario a eliminar: " nuevo_usuario

        if existe_usuario "$nuevo_usuario"; then
            echo "El usuario no existe." 
        else
            if sudo deluser "$nuevo_usuario"; then
                echo "Usuario $nuevo_usuario eliminado correctamente."
            else
                echo "Error al eliminar usuario."
            fi
        fi
    else
         echo "No tiene permiso de administrador."
    fi
}

function gestion_de_usuarios() {
    while true; do 
        echo ""
        echo "Menú de gestión de usuarios"
        echo "A. Añadir"
        echo "E. Eliminar"
        echo "V. Volver"
        read -p "Elige una opción: " opcion

        respuesta=$(validar_opcion $opcion "^[AaEeVv]$" "(A,E,V)")
        case $respuesta in 
            A) agregar_usuario ;; 
            E) eliminar_usuario ;; 
            V) return ;; 
        esac
    done
}