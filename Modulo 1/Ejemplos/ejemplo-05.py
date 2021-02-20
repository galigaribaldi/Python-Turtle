"""
@author: Galileo garibaldi
@date: 19/02/2021
@description: Modulo 1 Manejando Listas y Tuplas
"""

##Lista exclusivamente de números
listaNumeros = [10,20,30,40,50]

##Accediedno a un elemento en las listas
print("Accediendo al elemento 0: ", listaNumeros[0])
print("Accediendo al elemento 1: ", listaNumeros[1])

##Lista exclusivamente de Cadenas de texto
listaCadenas = ["Cadena 1", "Cadena 2", "Cadena 3"]

##Accediedno a un elemento en las listas
print("Accediendo al elemento 0: ", listaCadenas[0])
print("Accediendo al elemento 1: ", listaCadenas[1])

##Lista con diferentes tipos de valores
listaMixta = ["Cadena 1", 200, 30.1, True]

##Accediedno a un elemento en las listas
print("Accediendo al elemento 0: ", listaMixta[0])
print("Accediendo al elemento 1: ", listaMixta[1])
print("Accediendo al elemento 1: ", listaMixta[2])
print("Accediendo al elemento 1: ", listaMixta[3])

####Tuplas
tupla1 = (1,2,3,4)
tupla2 = (1,)


###Operaciones con listas

###Agregar al final
lista1 = [1,2,3]
print("Lista Vieja: ", lista1)
lista1.append(4)
print("Lista Nueva: ", lista1)

###Quitar Valores al final
print("Lista Vieja: ", lista1)
lista1.pop()
print("Lista Nueva: ", lista1)

###Contar numero de elementos
print("Existen ",lista1.count(1), " Numeros 1")

###Generar una copia de la lista
lista2 = lista1.copy()