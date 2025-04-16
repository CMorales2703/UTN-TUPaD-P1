#!/bin/bash
agenda="agenda.txt"
clear

# encierro todo el programa en un bucle, para que solo termine al seleccionar la opcion 3
while [[ ! "$opcion_nivel1" =~ ^[3]$ ]]; do
    echo "1. Ver club"
    echo "2. Gestionar"
    echo "3. Salir"
    read -p "Elige una opción: " opcion_nivel1
    echo ""

    while [[ ! "$opcion_nivel1" =~ ^[1,2,3]$ ]]; do
        read -p "Por favor, introduce una opción válida (1,2,3): " opcion_nivel1
    done

    # opción 1
    if [[ "$opcion_nivel1" -eq 1 ]]; then
        read -p "Ingrese el club: " club
        # pasamos el valor de club a mayuscula
        club=${club^^}

        # se ejecuta grep buscando si club existe en agenda
        if grep -iq "^$club," "$agenda"; then
            # si existe, muestra la informacion de toda la linea
            grep "^$club," "$agenda"  
        else
            echo "No se encontró el club"
        fi
        echo ""
    fi
    
    # opción 2
    if [[ "$opcion_nivel1" -eq 2 ]]; then
        # muestra el submenu
        echo "1. Insertar club"
        echo "2. Eliminar club"
        echo "3. Modificar club"
        echo "4. Salir"
        read -p "Elige una opción: " opcion
        echo ""

        # verifica que las opción ingresada sea la correcta
        while [[ ! "$opcion" =~ ^[1,2,3,4]$ ]]; do
            read -p "Por favor, introduce una opción válida (1,2,3,4): " opcion
        done
        
        # opción 1
        if [[ "$opcion" -eq 1 ]]; then
            read -p "Ingrese el club: " club
            club=${club^^}

            # busca el club en agenda, si existe lo informa
            if grep -iq "^$club," "$agenda"; then
                echo "Este club ya existe en la agenda"
            else
                # si no existe, pide el ingreso de los datos provincia, localidad, codido
                read -p "Ingrese el nombre de su provincia: " provincia
                provincia=${provincia^^}

                read -p "Ingrese su localidad: " localidad
                localidad=${localidad^^}

                read -p "Ingrese su codigo: " codigo
                codigo=${codigo^^}

                # agregamos toda la informacion a agenda
                echo "$club,$provincia,$localidad,$codigo" >> $agenda
                echo "Club agregado exitosamente"
            fi
        echo ""
        fi

        # opcion 2
        if [[ "$opcion" -eq 2 ]]; then
            read -p "Ingrese el club: " club
            club=${club^^}

            # busca si club se encuentra en agenda
            if grep -iq "^$club," "$agenda"; then
                # si lo encuentra, elimina toda la linea del club
                sed -i "/^$club,/d" $agenda
                echo "Club eliminado exitosamente"
            else
                # si no lo encuentra, lo informa
                echo "Este club no existe en la agenda"
            fi
        echo ""
        fi

        # opcion 3
        if [[ "$opcion" -eq 3 ]]; then
            read -p "Ingrese el club: " club
            club=${club^^}

             # busca si club se encuentra en agenda
            if grep -iq "^$club," "$agenda"; then
                # si lo encuentra, primero elimina la linea de ese club
                sed -i "/^$club,/d" $agenda

                # luego pide los datos provincia, localidad, y codigo
                read -p "Ingrese el nombre de su provincia: " provincia
                provincia=${provincia^^}

                read -p "Ingrese su localidad: " localidad
                localidad=${localidad^^}

                read -p "Ingrese su codigo: " codigo
                codigo=${codigo^^}
                
                # agregamos toda la informacion a agenda
                echo "$club,$provincia,$localidad,$codigo" >> $agenda
                echo "Club modificado exitosamente"
                
            else
                echo "Este club no existe en la agenda"
            fi
        echo ""
        fi

         # opción 4, vuelve al menu principal
        if [[ "$opcion_nivel1" -eq 4 ]]; then
            return
        fi
    fi

    # opción 3, sale del programa
    if [[ "$opcion_nivel1" -eq 3 ]]; then
        echo "Hasta Luego!"
    fi

done