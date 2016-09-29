#!/usr/bin/env python
# -*- coding: utf-8 -*-


#Realice un programa que permita ingresar los datos de alumnos de una facultad
#. Por cada alumno se ingresa: nombre, apellido, genero, edad, carrera.
#El ingreso de dato finaliza cuando se ingresa la edad -1. Se solicita
#que informe: a) La cantidad mujeres se inscribieron en la carrera de
#informática y su promedio de edad. b) La cantidad de hombres de entre 17 y
#20 años de edad inscriptos en química.

nombre = ""
apellido = ""
genero = ""
edad = 0
carrera = ""
cantm = 0
cantf = 0
sumaed = 0
prom = 0.0

alumnos = input("Ingrese la cantidad de alumnos")

for i in range(alumnos):

#        nombre = raw_input ("Ingrese nombre del alumno: ")
#        apellido = raw_input ("Ingrese Apellido: ")
        genero = raw_input ("Ingrese Sexo: ")
        edad = input ("Ingrese edad: ")
        if edad == -1:
            break
        carrera = raw_input ("Ingrese Carrera: ")

        if genero == "femenino" and carrera == "informatica":
            cantf = cantf + 1
            sumaed = sumaed + edad
        if genero == "masculino" and carrera =="quimica":
            if  20 > edad > 17:
                cantm = cantm + 1

prom = float(sumaed / cantf)

print cantf
print sumaed
print prom
print cantm
