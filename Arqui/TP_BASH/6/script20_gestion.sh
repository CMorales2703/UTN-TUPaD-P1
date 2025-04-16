#!/bin/bash

# función que imprime si el usuario existe
function Informacion_usuario(){
    read -p "Ingrese el nombre del usuario: " usuario

    # llamada la función, en caso de no existir, muestre mensaje
    if existe_usuario "$usuario"; then
        echo "El usuario no existe"
    else
        # si el usuario existe, usa finger para mostrar la info del mismo
        echo "Usuario encontrado"
        finger "$usuario"
    fi
}

# función que verifica si el usuario existe
function existe_usuario(){
    local usuario=$1

    # si da 0 no existe
    if ! id "$usuario" &>/dev/null; then
        return 0  
    else
    # si da 1, si existe
        return 1  
    fi
}

# función para validar las opciones, recibe como parametros la opción elegida, el criterio de comparacion y las opciones para mostrar en pantalla en caso de error
function validar_opcion(){ 
    local opcion=$1
    local criterios=$2
    local opciones=$3

    while [[ ! "$opcion" =~ $criterios ]]; do
        read -p "Por favor, introduce una opción válida $opciones: " opcion
    done
    # devuelve la opción correcta
    echo "${opcion^^}"
}

# función para agregar un usuario
function agregar_usuario(){ 
    # verifica si el usuario actual pertenece al grupo sudo
    if groups "$USER" | grep -q '\bsudo\b'; then
        # pide el nombre del nuevo usuario
        read -p "Nombre del usuario: " nuevo_usuario

        # llamada a la función para verificar si el usuario existe
        if existe_usuario "$nuevo_usuario"; then
            echo "El usuario no existe." 
            # si no existe, intenta crearlo con sudo
            if sudo adduser "$nuevo_usuario"; then
                echo "Usuario $nuevo_usuario creado correctamente."
            else
                echo "Error al crear usuario."
            fi
        else
            # si el usuario ya existe, lo informa
            echo "El usuario ya existe."
        fi
    else
        # si el usuario actual no tiene permisos de administrador
        echo "No tiene permiso de administrador."  
    fi
}


# función para eliminar un usuario
function eliminar_usuario(){
    # verifica si el usuario actual pertenece al grupo sudo
    if groups "$USER" | grep -q '\bsudo\b'; then
        # pide el nombre del usuario a eliminar
        read -p "Nombre del usuario a eliminar: " nuevo_usuario

         # llamada a la función para verificar si el usuario existe
        if existe_usuario "$nuevo_usuario"; then
            echo "El usuario no existe." 
        else
            # si existe, intenta eliminarlo con sudo
            if sudo deluser "$nuevo_usuario"; then
                echo "Usuario $nuevo_usuario eliminado correctamente."
            else
                echo "Error al eliminar usuario."
            fi
        fi
    else
        # si el usuario actual no tiene permisos de administrador
        echo "No tiene permiso de administrador."
    fi
}


# función que muestra el menú de gestión de usuarios
function gestion_de_usuarios() {
    # bucle infinito para mantener el menú hasta que se elija la opción volver
    while true; do 
        echo ""
        echo "Menú de gestión de usuarios"
        echo "A. Añadir"
        echo "E. Eliminar"
        echo "V. Volver"
        read -p "Elige una opción: " opcion

        # llamada a la función para validar la opción ingresada (A, E o V)
        respuesta=$(validar_opcion $opcion "^[AaEeVv]$" "(A,E,V)")

        # ejecuta la acción correspondiente
        case $respuesta in 
            # llama a la función para agregar usuario
            A) agregar_usuario ;;   
            # llama a la función para eliminar usuario
            E) eliminar_usuario ;;  
            # sale del menú (vuelve al menú principal)
            V) return ;;            
        esac
    done
}