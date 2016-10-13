#!/usr/bin/env python
# -*- coding: utf-8 -*

#!/usr/bin/env python
# -*- coding: utf-8 -*

#Realice un programa que lea las calificaciones de un curso y muestre
#el promedio y la nota mas alta.La lectura de notas finaliza cuando se
#ingresa un valor negativo.

#Agregarle la funcionalidad de saber la cantidad de alumnos
#que superan al promedio

alta = 0
suma = 0.0
cant = 0
conjunto = ""
losdiez = ""
alumnosup = 0

nota = int(input('Ingrese las notas del curso: '))
while nota > 0:
    suma = suma + nota
    cant = cant + 1
    if nota == 10:
        losdiez = losdiez + str(nota)
        alumnosup = alumnosup + 1
    else:
        conjunto = conjunto + str(nota)
    if nota > alta:
        alta = nota

    nota = int(input('Ingrese valor (negativo para salir)'))
print('El promedio de las notas es', suma / cant)
print("La nota mas alta es", alta)

for c in conjunto:
    if int(c) > (suma / cant):
        alumnosup = alumnosup + 1

print("Los alumnos que superan el promedio general son :", alumnosup)
