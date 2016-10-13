#!/usr/bin/env python
# -*- coding: utf-8 -*


#Se lee una cadena de caracteres por teclado y se pide que la traduzca a
#código morse utilizando el siguiente diccionario como base:

morse = {"A": ".-", "B": "-...", "C": "-.-.", "D": "-..",
         "E": ".", "F": "..-.", "G": "--.", "H": "....", "I": "..",
         "J": ".---", "K": "-.-", "L": ".-..", "M": "--", "N": "-.",
         "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...",
         "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
         "Y": "-.--", "Z": "--..", "0": "-----", "1": ".----",
         "2": "..---", "3": "...--", "4": "....-", "5": ".....",
         "6": "-....", "7": "--...", "8": "---..", "9": "----.",
         ".": ".-.-.-", ",": "--..--"}

palabra = ""
cifrada = ""

palabra = raw_input ("Ingrese la palabra a pasar a codigo morse: ")

for letra in palabra:
    for codigolet, cif in morse.items():
        if codigolet == letra:
            cifrada = cifrada + cif

print ("Esta es la palabra cifrada", cifrada)
