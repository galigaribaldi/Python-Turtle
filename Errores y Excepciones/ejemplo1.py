####error
"""while True:
print("hola")"""
####Excepciones
"""
10/0
("hola"+0)"""
#################################usando try -except:
"""
while True:
	x=int(input("por favor ingrese un numero"))
	break ###Lanza ValueError
"""

"""
try:
	f = open("miarchivo.txt")

except FileNotFoundError:
	print("No existe")
"""
try:
	print("algo")
	while 1:
	print("hola")
except IndentationError:
	print("Tu indentacion esta mal")


