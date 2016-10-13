#!/usr/bin/env python
# -*- coding: utf-8 -*

def cifrado(lpalabra):
    palabrac = ""
    for letra in lpalabra:
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

    return palabrac



palabra = ""
palabrac = ""
palabra = raw_input("Ingrese la palabra a cifrar: ")
palabrap = cifrado(palabra)
print(palabrap)

