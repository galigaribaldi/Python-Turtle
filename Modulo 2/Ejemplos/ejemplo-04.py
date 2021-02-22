"""
@author: Galileo garibaldi
@date: 20/02/2021
@description: Ejemplo 4
"""
###Definir la función
def funcion3(a):###Recibimos parametros
    a.append(1)
    a.append(2)
    a.append(3)
    return a
  
resultado = funcion3([1,2,3,4])
##imprime el resultado, pero no retorna nada
print(resultado)