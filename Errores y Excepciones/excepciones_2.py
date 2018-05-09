

def Modulos():
	try:
		import os
		import Tkinter
	except ModuleNotFoundError as error:
		print("Este mdoulo es para python 2.7, para la nueva versión es tkinter")
		print(error.args) ###paraimprimir argumentos
		import tkinter
	finally:
		print("Se limpiará la pantalla")
		os.system("cls")

######################################################

def leerArchivos():
	leer = input("Dime el nombre de tu archivo")
	Archi = leer +".txt"
	try:
		f = open(Archi)
		cadena= f.read()
		print(cadena)
	except FileNotFoundError:
		print("No existe")

