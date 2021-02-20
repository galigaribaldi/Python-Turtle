"""
@author: Galileo garibaldi
@date: 19/02/2021
@description: Modulo 1 operaciones entre tipos de dato
"""

###Tipos de dato numerico

###Tipo Int
varibaleInt = 34
variableInt2 = 45.2
print(varibaleInt, variableInt2)

##Para saber el tipo de dato que es, usamos type()
print("La variable variableInt es: ", type(varibaleInt))
print("La variable variableInt 2 es: ", type(variableInt2))

###Operaciones entre int

###Operaciones entre sumas
print("Suma: ", varibaleInt + variableInt2)
print("Suma con diferentes números: ", varibaleInt + 89)
###Operaciones entre resta
print("Resta: ", varibaleInt - variableInt2)
print("Resta con diferentes números: ", varibaleInt - 100)
###Operaciones entre Multiplicacion
print("Multiplicacion: ", varibaleInt * variableInt2)
print("Multiplicacion entre diferentes numeros: ", varibaleInt * 10)
###Operaciones entre division
print("Division: ", varibaleInt / variableInt2)
print("Division entre diferentes numeros: ", varibaleInt / 100)
#Si se divide entre 0, python marcarà un error
#print("Division entre diferentes numeros: ", varibaleInt / 0)

#####Tipos de dato Booleano
Variableverdadera = True
VariableFalsa = False

print("La variable 1 es: de tipo: ", type(Variableverdadera), " y contiene el valor: ", Variableverdadera)
print("La variable 2 es: de tipo: ", type(VariableFalsa), " y contiene el valor: ", VariableFalsa)