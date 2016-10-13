#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Abre archivo en modo append
archivo = open('/home/andres/Escritorio/Tecnicatura en Software Libre/Desarrollo de Software Libre/Unidad 4/archi01.txt', 'a')
# lista con los elementos a escribir
L = ['abril 33\n', 'mayo 21\n', 'junio 88\n']
archivo.writelines(L)
archivo.close()