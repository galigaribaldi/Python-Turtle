"""
Este codigo corre desde la consola
"""
###Suma
numero1=(input("Deme el primer numero a sumar: "))
numero2=(input("Deme el segundo numero a sumar: "))
suma3 = numero1+numero2
print("El resultado es: ", suma3)

###Resta
numero1=int(input("Deme el primer numero a restar: "))
numero2=int(input("Deme el segundo numero a restar: "))
resta = numero1-numero2
print("El resultado es: ", resta)

####multiplicación
numero1=int(input("Deme el primer numero a multiplicar: "))
numero2=int(input("Deme el segundo numero a multiplicar: "))
multiplicacion = numero1*numero2
print("El resultado es: ", multiplicacion)

###División
numero1=int(input("Deme el dividendo: "))
numero2=int(input("Deme el Divisor: "))
division = numero1/numero2
print("El resultado es: ", division)

###elevar a una potencia
numero1=int(input("Deme la base: "))
numero2=int(input("Deme el exponente: "))
potencia = numero1**numero2
print("El resultado es: ", potencia)

###Cociente de una division
numero1=int(input("Deme el dividendo: "))
numero2=int(input("Deme el Divisor: "))
division = numero1//numero2
print("El resultado es: ", division)

###operaciones mas avanzadas
def avanzados():
	import math
	raiz = math.sqrt(12)
	seno = math.sin(12)
	logaritmo = math.log(12)
	pi=math.pi
	print("la raiz cuadrada es: ", raiz)
	print("El seno de un numero es: ", seno)
	print("El logaritmo de un numero es:", logaritmo)
	print("El valor de pi es:", pi)
avanzados()