#!/bin/bash
clear

# imprime los valores de los parámetros
echo "Valor del primer parámetro: $1"
echo "Valor del segundo parámetro: $2"
echo "Valor del tercer parámetro: $3"
echo "Valor del cuarto parámetro: $4"
echo "Valor del quinto parámetro: $5"
echo "Valor del sexto parámetro: $6"
echo "Valor del séptimo parámetro: $7"
echo "Valor del octavo parámetro: $8"
echo "Valor del noveno parámetro: $9"

# muestra el total de parámetros
echo "Total de parámetros recibidos: $#"

# muestra los parámetros concatenados
echo "Todos los parámetros concatenados: $*"

# muestra el nombre del archivo
echo "Nombre del archivo ejecutado utilizando $0"