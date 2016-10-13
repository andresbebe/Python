#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Crea archivo en modo escritura
archivo = open('/home/andres/Escritorio/Tecnicatura en Software Libre/Desarrollo de Software Libre/Unidad 4/archi02.txt', 'w')
# Contenido a almacenar en archivo
linea1 = 'nace una flor\n'
linea2 = 'todos los dias\n'
linea3 = 'sale el sol\n'
# Escritura en archivo de cada linea
archivo.write(linea1)
archivo.write(linea2)
archivo.write(linea3)
archivo.close()