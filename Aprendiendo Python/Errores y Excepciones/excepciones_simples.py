
while True:
	try:
		x = int(input("por favor ingrese un numero: "))
	except ValueError:
		print("Eso no es un numero")

while True:
	try:
		x = int(input("por favor ingrese un numero: "))
	except ValueError:
		print("Eso no es un numero")
	except KeyboardInterrupt:
		print("No puedes salir por Ctrl + c")
