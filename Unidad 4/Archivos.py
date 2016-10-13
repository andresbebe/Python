#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Ejemplo de Archivo apertura y modo leectura

# Apertura del archivo en modo lectura

f = open('/home/andres/Escritorio/Tecnicatura en Software Libre/Desarrollo de Software Libre/Unidad 4/archi01.txt', 'r')

# Lee la primer línea
r = f.readline()
print(r)

# Lee la segunda línea
r = f.readline()
print(r)

# Cierra el archivo
f.close()