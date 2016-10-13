#!/usr/bin/env python
# -*- coding: utf-8 -*

#Este bucle lo que hace es: Se ingresan valores hasta que
#Se ingrese uno negativo el cual corta el ciclo comprobando
# en el While el valor ingresado dentro del mismo.
#

suma = 0.0
cant = 0
x = int(input('Ingrese valor (negativo para salir)'))
while x > 0:
        suma = suma + x
        cant = cant + 1
        x = int(input('Ingrese valor (negativo para salir)'))
print('El promedio de valores es', suma / cant)