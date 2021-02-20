"""
@author: Galileo garibaldi
@date: 19/02/2021
@description: Modulo 1 Manejando Diccionarios
"""
diccionario = {1:"Valor 1", 2: "Valor 2", "Llave 1": "Valor 1"}
###Acceder a un diccionario por su llave
print("El valor 1: ", diccionario[1])
print("El valor 2: ", diccionario[2])
print("Obteniendo todas las llaves: ", diccionario.keys())
print("Obteniendo todas los Valores: ", diccionario.values())
##Modificando un valor por su llave
diccionario[1] = 1
print("El valor 1: ",diccionario[1] )