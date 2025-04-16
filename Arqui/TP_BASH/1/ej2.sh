#!/bin/bash
clear

read -p "usuario: " usuario
read -p "mensaje: " mensaje

# con redireccionamiento
echo $mensaje >mensaje.txt
write $usuario <mensaje.txt

# con pipe
echo $mensaje | write $usuario