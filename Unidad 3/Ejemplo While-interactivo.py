#!/usr/bin/env python
# -*- coding: utf-8 -*

#While interactivo , mientras la condicion no cambie en el ciclo no se rompe
#Se declara suma , cant y mas_datos con "si"
#Inicia con si para que inicie el ciclo
#Por cada vez que recorre el ciclo pregunta al final si hay mas valores para
#Ingresar. Si se pone si continua si no no.
#Mientras suma y cuenta los valores ingresados  con suma = suma + x
# y con cant = cant + 1

suma = 0.0
cant = 0
mas_datos = "si"

while mas_datos == 'si':
    x = int(input('Ingrese valor'))
    suma = suma + x
    cant = cant + 1
    mas_datos = raw_input('¿Mas valores (si/no)?')
    print('El promedio de valores es', suma / cant)