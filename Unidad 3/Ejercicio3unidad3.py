#!/usr/bin/env python
# -*- coding: utf-8 -*

#Realice un programa que lea las calificaciones de un curso y muestre
#el promedio y la nota mas alta.La lectura de notas finaliza cuando se
#ingresa un valor negativo.

alta = 0
suma = 0.0
cant = 0

nota = int(input('Ingrese las notas del curso: '))
while nota > 0:
    suma = suma + nota
    cant = cant + 1
    if nota > alta:
        alta = nota

    nota = int(input('Ingrese valor (negativo para salir)'))
print('El promedio de las notas es', suma / cant)
print("La nota mas alta es", alta)