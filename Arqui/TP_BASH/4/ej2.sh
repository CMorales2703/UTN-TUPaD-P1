#!/bin/bash
agenda="agenda.txt"
clear

while [[ ! "$opcion_nivel1" =~ ^[3]$ ]]; do
    echo "1. Ver club"
    echo "2. Gestionar"
    echo "3. Salir"
    read -p "Elige una opción: " opcion_nivel1
    echo ""

    while [[ ! "$opcion_nivel1" =~ ^[1,2,3]$ ]]; do
        read -p "Por favor, introduce una opción válida (1,2,3): " opcion_nivel1
    done

    if [[ "$opcion_nivel1" -eq 1 ]]; then
        read -p "Ingrese el club: " club
        club=${club^^}

        # Ejecutamos grep y verificamos el resultado
        if grep -iq "^$club," "$agenda"; then
            grep "^$club," "$agenda"  # Mostrar los detalles si se encontró
        else
            echo "No se encontró el club"
        fi
        echo ""
    fi

    if [[ "$opcion_nivel1" -eq 2 ]]; then
        echo "1. Insertar club"
        echo "2. Eliminar club"
        echo "3. Modificar club"
        echo "4. Salir"
        read -p "Elige una opción: " opcion
        echo ""

        while [[ ! "$opcion" =~ ^[1,2,3,4]$ ]]; do
            read -p "Por favor, introduce una opción válida (1,2,3,4): " opcion
        done
        
        if [[ "$opcion" -eq 1 ]]; then
            read -p "Ingrese el club: " club
            club=${club^^}

            if grep -iq "^$club," "$agenda"; then
                echo "Este club ya existe en la agenda"
            else
                read -p "Ingrese el nombre de su provincia: " provincia
                provincia=${provincia^^}

                read -p "Ingrese su localidad: " localidad
                localidad=${localidad^^}

                read -p "Ingrese su codigo: " codigo
                codigo=${codigo^^}

                echo "$club,$provincia,$localidad,$codigo" >> $agenda
                echo "Club agregado exitosamente"
            fi
        echo ""
        fi

        if [[ "$opcion" -eq 2 ]]; then
            read -p "Ingrese el club: " club
            club=${club^^}

            if grep -iq "^$club," "$agenda"; then
                sed -i "/^$club,/d" $agenda
                echo "Club eliminado exitosamente"
            else
                echo "Este club no existe en la agenda"
            fi
        echo ""
        fi

        if [[ "$opcion" -eq 3 ]]; then
            read -p "Ingrese el club: " club
            club=${club^^}

            if grep -iq "^$club," "$agenda"; then
                sed -i "/^$club,/d" $agenda
                read -p "Ingrese el nombre de su provincia: " provincia
                provincia=${provincia^^}

                read -p "Ingrese su localidad: " localidad
                localidad=${localidad^^}

                read -p "Ingrese su codigo: " codigo
                codigo=${codigo^^}

                echo "$club,$provincia,$localidad,$codigo" >> $agenda
                echo "Club modificado exitosamente"
                
            else
                echo "Este club no existe en la agenda"
            fi
        echo ""
        fi

    fi

    if [[ "$opcion_nivel1" -eq 3 ]]; then
        echo "Hasta Luego!"
    fi

done