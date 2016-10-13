#!/usr/bin/env python
# -*- coding: utf-8 -*-


#Escriba un programa que lea un archivo con temperaturas expresadas
#en grados centigrados, y que luego genere otro archivo que contenga
#dichas temperaturas pero expresadas en grado Fahrenheit.
#Como archivo de entrada, utilice el siguiente:

#Apertura del archivo en modo lectura y archivof en escritura

archivo = open('/home/andres/Escritorio/Tecnicatura en Software Libre/Desarrollo de Software Libre/Unidad 4/tempk.txt', 'r')
archivof = open('/home/andres/Escritorio/Tecnicatura en Software Libre/Desarrollo de Software Libre/Unidad 4/tempf.txt', 'w')

# Lee todo el achivo

lineas = archivo.readlines()


def pasajegradosk(k):
    fa =(9 *(k-273.15)/5.0) +32
    return fa

def pasajegrados(t):
    f = 9 / 5.0 * t + 32
    return f

for linea in lineas:
    g, val = linea.split()
    if val == "oC":
        l = float(g)
        s = pasajegrados(l)
        f = str(s) + " °F" + "\n"
        print (f)
        archivof.write(f)
    elif val == "oK":
        l2 = float(g)
        s2 = pasajegradosk(l2)
        f2 = str(s2) + "°F" + "\n"
        print(f2)
        archivof.write(f)
    elif val == "oF":
        f3 = str(g) + "°F" + "\n"
        print(f3)
        archivof.write(f3)



archivo.close()
archivof.close()












