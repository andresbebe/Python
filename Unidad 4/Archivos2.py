#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Ejemplo de Archivo apertura y modo leectura
# Apertura del archivo en modo lectura con while

# Apertura del archivo en modo lectura

archivo = open('/home/andres/Escritorio/Tecnicatura en Software Libre/Desarrollo de Software Libre/Unidad 4/archi01.txt', 'r')

# Lee la primer línea

linea = archivo.readline()

while linea:
    print(linea)
# lee la sgte
    linea = archivo.readline()
archivo.close()
