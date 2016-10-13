
#!/usr/bin/env python
# -*- coding: utf-8 -*

#Almacene 10 nombres de personas en una lista que son ingresados por teclado.
#Muestre por pantalla la lista original, ordenada, en sentido inverso, y pase
#a mayusculas la primer letra. Ademas, permita ingresar un nombre que sea
#eliminado de la lista y muestre el resultado de la eliminacion o un mensaje
#alusivo si no fue posible la eliminacion.

#NOTA La lista sigue siendo la misma


#Declaramos variables 2 string y una lista
eliminar = ""
palabra = ""
listanom = []

# ciclo de 3 personas y usamos el metodo append para agregar items a la lista
for i in range(3):
    listanom.append(raw_input ("Ingrese nombre de la persona: "))

#Imprimimos la lista ingresada
print("Lista ingresada: ", listanom)

#Imprimimos la lista aplicando el metodo reverse (orden inverso)
print("Lista inversa: ", listanom.reverse())

#Ciclo for y range usando len sobre la lista que tenemos que son 3 items
#Metemos en una variable el item de la lista que estamos iterando en este caso
#es letra.
#
for letra in range(len(listanom)):
    palabra = listanom[letra]
#Una vez que tenemos el item en palabra ,un string con los corchetes nos
#paramos en la posicion 0 la primera posicion y le sumamos todo lo que viene
#entre la posicion 1 en adelante e imprimimos.

    palabra = palabra[0].upper() + palabra[1:]
    print (palabra)

#Esto es para aclarar que se utilizo la variable y se fue imprimiendo
#No se metio en otra lista
print ("Como quedo la lista", listanom)

# Se ingresa el valor a eliminar , se recorre listanom y se compara el item
#x que estamos iterando con eliminar si coincide se elimina.
#Se utiliza el metodo remove para eliminar el item. Y se imprime un mensaje
#de operacion exitosa.

eliminar = raw_input("Ingrese el nombre de la persona a eliminar: ")
for x in listanom:
    if x == eliminar:
        listanom.remove(x)
        print ("Se elimino de forma exitosa: ")

print(listanom)