#!/usr/bin/env python
# -*- coding: utf-8 -*

#Utilice una estructura repetitiva for para iterar sobre las letras
#de una palabra y muestre en pantalla su versión encriptada.
#Para encriptarla imprima en pantalla el reemplazo de una letra con un número
#según lo siguiente: a->4, b->8, e->3, f->7, t->2, g->9, i->1, o->0.

palabrac = ""
palabra = raw_input("Ingrese la palabra a cifrar: ")
for letra in palabra:
    if letra == "a":
        palabrac = palabrac + "4"
    elif letra == "b":
        palabrac = palabrac + "8"
    elif letra == "e":
        palabrac = palabrac + "3"
    elif letra == "f":
        palabrac = palabrac + "7"
    elif letra == "t":
        palabrac = palabrac + "2"
    elif letra == "g":
        palabrac = palabrac + "9"
    elif letra == "i":
        palabrac = palabrac + "1"
    elif letra == "o":
        palabrac = palabrac + "0"
    else:
        palabrac = palabrac + letra
print ("La palabra cifrada es", palabrac)