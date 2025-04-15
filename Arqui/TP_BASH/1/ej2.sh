#!/bin/bash
clear
echo -n "Mensaje para todos los usuarios: "
read mensaje

# Enviar mensaje a todos los usuarios conectados
echo "$mensaje" | wall