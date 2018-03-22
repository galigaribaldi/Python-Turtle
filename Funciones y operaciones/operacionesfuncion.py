numero1=int(input("Numero 1: "))
numero2=int(input("Numero 2: "))

def Suma(numero1, numero2):
	resultado= numero1+numero2
	print(resultado)

def Resta(numero1, numero2):
	resultado = numero1 - numero2
	print(resultado)

def Multiplicacion(numero1, numero2):
	resultado = numero1 * numero2
	print(resultado)

def Division(numero1, numero2):
	resultado = numero1/numero2
	print(resultado)

def Raiz():
	import math
	numero1 = int(input("Raiz de un numero: "))
	math.sqrt(numero1)
	print(numero1)