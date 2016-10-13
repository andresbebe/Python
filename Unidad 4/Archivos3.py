#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Apertura del archivo en modo lectura

archivo = open('/home/andres/Escritorio/Tecnicatura en Software Libre/Desarrollo de Software Libre/Unidad 4/archi01.txt', 'r')

# Lee todo el achivo

lineas = archivo.readlines()

# para promedio

suma = 0
cant = 0

# itera sobre lista lineas

for linea in lineas:
    mes, val = linea.split()  # separo por espacio
    suma = suma + int(val)  # sumo convirtiendo a entero
    cant = cant + 1  # cuento los valores

archivo.close()
promedio = suma / cant
print('Promedio: ', promedio)