#!/usr/bin/env python
# -*- coding: utf-8 -*-


#Intercambio de variables:

#Se declara una variable auxiliar,
#se guarda la edad1 temporal, se pisa la edad 1
#con la edad 2 y se pisa la edad2 con el la variable auxiliar.

nombre1 = raw_input ("Ingrese el nombre de la primera persona: ")
nombre2 = raw_input ("Ingrese el nombre de la segunda persona: ")
edad1 = raw_input ("Ingrese la edad de la primera persona: ")
edad2 = raw_input ("Ingrese la edad de la segunda persona: ")

print ("El nombre de la primera persona es: " + " " + nombre1 + "" + " y su edad es " + edad1 + " años")
print ("El nombre de la segunda persona es: " + " " + nombre2 + "" + " y su edad es " + edad2 + " años")


aux = edad1
edad1 = edad2
edad2 = aux

print ("El nombre de la primera persona es: " + " " + nombre1 + "" + " y su edad es " + edad1 + " años")
print ("El nombre de la segunda persona es: " + " " + nombre2 + "" + " y su edad es " + edad2 + " años")