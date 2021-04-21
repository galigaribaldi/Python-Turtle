# Módulo 3 (Módulo Tortugas)

En este módulo se revisará a fondo el uso de la librería tortugas, está viene incluida en el paquete oficial de python y no se debe realizar ninguna instalación adicional.

*Gráficas Turtle es una forma muy habitual de introducción a la programación para niñas y niños. Era parte original del lenguaje de programación Logo, desarrollado por Wally Feurzeig, Seymour Papert y Cynthia Solomon en 1967.* Esto quiere decir que el módulo tortugas es una forma sencilla dee aprender a programar y darle instrucciones a un prototipo de *robot*

En caso de necesitar instalat algo adicional, se recomienda hacer uso de la terminal e instalar los paquete marcados

**Paquete Base Turtle**

```shell
pip install turtle
```
**Paquete Base Tkinter**
```shell
pip install tkinter
```
**El siguiente es solo en el caso de estar usando google Colab**
```shell
pip install ColabTurtle
```

## 1.- Comandos Básicos

### 1.1.-Avanzar y Girar

Para este primer caso, sólo se requiere importar la librería tortugas, esto se puede hacer de 2 formas, a continuación veremos la primera forma.

- Forma 1, importando toda la librería

  - ```python
    from turtle import *
    ```

- Forma 2, importando sólo lo necesario

  - ```python
    import turtle
    ```

**En algunos casos será necesario usar una forma en esepcifico para sacar mejor provecho a este módulo**

Una vez que tenemos importado el módulo tortugas, lo siguiente que haremos será indicarle la dirección hacía donde esta se dirigirá, la tortuga, esto lo haremos con comandos y giros básicos. A continuación se detalla las coordenadas y orieentación que sigue la tortuga para hacer sus movimientos

<img src="https://i1.wp.com/copyassignment.com/wp-content/uploads/2020/12/X-1.png?w=1080&ssl=1" alt="Coordenadas" style="zoom:50%;" />

Los comandos que se usarán para poder mover la tortuga de forma básica serán:

- **forward(numero_de_casillas_avanzar):** Numero de casillas a avanzar, esto nos permite que nuestra tortuga avance una cantidad de espacios determinados
  - Este comando también se puede abreviar a *fd*
- **left(numero_de_casillas_girar):** Numero de casillas a girar, estos giros siempre se dan en torno a 360º, cuando se indica la palabra *left*, se está diciendo que se gire hacia la izquierda
  - Este comando también se puede abreviar a *lt*
- **right(numero_de_casillas_girar):** Numero de casillas a girar, estos giros siempre se dan en torno a 360º, cuando se indica la palabra *right*, se está diciendo que se gire hacia la derecha
  - Este comando también se puede abreviar a *rt*
- **shape(forma_tortuga):** Adicionalmente podemos elegir entre 3 formas de nuestra tortuga
  - **turtle**: Nos permite ver una tortuga moviéndose
  - **circle**: Nos permite ver una círculo moviéndose
  - **arrow**: Nos permite ver una triángulo moviéndose

#### Código Final

A continación se describe el código final

```python
#### Basico sin usar funciones
from turtle import *
shape("turtle")
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
#input() ##Opcional si se requieree poner una pausa
```

### 1.2.-Ordenar Tu código

Por lo regular siempre será bueno que el código se divida en pequeñas funciones que hagan una tarea específica, de esta forma, podemos darle mayor congruencia a nuestro código y posteriormente a nuestras ideas

A continuación se describe la estructura básica de una función

```python
def nombre_funcion(parametros):
  ##todo lo que haga mi función
  return 
```

**Partes de mi función**:

- ```python
  def nombre_funcion
  ```

  - En estas líneas dee código se usa la palabra reservada *def*, la cual sirve para indicarle a python que estamos por definir una función, la cual va acompañada por nuestro nombre de la función *nombre_funcion*, este nombre es definido por nosotros

- ```python
  def nombre_funcion(parametros):
  ```

  - En algunos casos necesitaremos agregarle parámetros a nuestras funciones, es deecir que reciban datos, estos datos pueden ser de tipo *int*, *string*, *float* o bien una lista o tupla, estos van dentro de los paréntesis y sólo viven dentro de nuestra función

- ```python
  def nombre_funcion(parametros):
    ##todo lo que haga mi función
    return
  ```

  - En estas últimas líneas podemos notar que se dejan 4 espacios entre el inicio de mi función y el inicio del código que pertenece a mi función, de esta forma, podemos decir que eel código alojado dentro de mi función, sólo y únicamente vive dentro de mi función. A estos 4 espacios se les conoce como **identación**

#### Creando un Cuadrado

Para esta parte se creará un cuadrado utilizando lo anteriormente visto

```python
def cuadrado():    
    shape("turtle")
    forward(100)
    left(90)
    forward(100)
    left(90)
    forward(100)
    left(90)
    forward(100)
    left(90)
```

**¡¡¡Importante!!!:** Cada vez que se cree una función no basta con sólo crearla, también hace falta mandarla a llamar, esto lo conseguimos escribiendo el nombre de la función fuera de la misma, dándole a entender a python que la mandaremos a llamar

```python
def cuadrado():    
    shape("turtle")
    forward(100)
    left(90)
    forward(100)
    left(90)
    forward(100)
    left(90)
    forward(100)
    left(90)
cuadrado()
```

#### Creando un Triángulo

Para este caso se necesita un giro diferente y un numero diferente de pasos a dar, ya que la figura tiene 3 lados, se darán solo 3 *forward*

```python
def triangulo():    
    shape("turtle")
    forward(100)
    left(120)
    forward(100)
    left(120)
    forward(100)
    left(120)
triangulo()
```

### 1.3.-Configurar Tu tortuga

#### Tamaño de la figura

El tamaño de la figura puede ser modificado de la siguiente forma

```python
shapesize(2) ###Tamaño de la figura
```

Esto nos permite agrandar o hacer mas pequeña nuestra tortuga, el numero que va dentro del parentesís, puede ser un número entero, sin embargo se recomienda no hacer el numero tan grande, ya que podría ser contraproducente

#### Color de la pluma (línea)

Para este caso sólo se colorea el borde de la pluma, es decir del trazo, no se colorea el interior

```python
pencolor("green") ###Color de la tortuga
```

El color que va entre los parentesís debe ser un color en inglés, sin embargo este puede ser cualquiera de los colores válidos que se muestran a continuación: https://trinket.io/docs/colors

#### Grosor de la pluma (línea)

En este caso se verá el grosor de la pluma y por consiguiente el grosor del trazo

```python
pensize(2) ##Grosor de la tortuga
```

Esto nos permite agrandar o hacer mas pequeño el trazo de la tortuga, el numero que va dentro del parentesís, puede ser un número entero, sin embargo se recomienda no hacer el numero tan grande, ya que podría ser contraproducente

#### Relleno del trazo 

Para este caso particular se usan 3 líneas de código, cada una con una utilidad diferente

```python
color("green", "blue") ###Primer argumento linea de color, segundo argumento Color de relleno
```

Si no se define un segundo color, se tomará de default que el relleno será del mismo

**Marcar el comienzo de relleno:** Se debe poner estas líneas cuando se marca el inicio de la figura o trazo que se va a rellenar

```python
begin_fill()###Marcar inicio de relleno
```

**Marcar el fin de relleno:** Se debe poner estas líneas cuando se marca el Fin de la figura o trazo que se va a rellenar, este en automático coloreara del color definido en las líneas anteriores

```python
end_fill() ###fin de relleno
```

#### Código Completo

```python
##Creando una tortuga personalizada
from turtle import *
shape("turtle") ##forma de la tortuga
shapesize(2) ###Tamaño de la fugura
pencolor("green") ###Color de la tortuga
pensize(2) ##Grosor de la tortuga
def cuadrado():
    ##Emepezar a rellenar 
    frank.color("green", "blue") ###Primer argumento linea de color, segundo argumento Color de relleno
    frank.begin_fill()###Marcar inicio de relleno
    ###Creando un cuadrado
    frank.fd(100)
    frank.lt(90)
    frank.fd(100)
    frank.lt(90)
    frank.fd(100)
    frank.lt(90)
    frank.fd(100)
    frank.end_fill() ###fin de relleno
    input()
```

## 2.- Generando una Tortuga Propia

Para este tramo crearemos un objeto de tipo tortuga, es decir haremos un clon de la estructura original, esto nos da la capacidad de modificar, crear y clonar varias tortugas para un mismo programa, esto se traduce que tendríamos varios pinceles funcionando.

```python
##Creando una tortuga personalizada
import turtle
##Creando una tortuha con nombre
frank = turtle.Turtle() 
frank.shape("turtle") ##forma de la tortuga
frank.shapesize(2) ###Tamaño de la fugura
frank.pencolor("green") ###Color de la tortuga
frank.pensize(2) ##Grosor de la tortuga
```

En el tramo anterior se describe la configuración de la tortuga, de manera que ésta pueda ser personalizada al gusto que se decida

**Código Completo**

```python
##Creando una tortuga personalizada
import turtle
##Creando una tortuha con nombre
frank = turtle.Turtle()
frank.shape("turtle") ##forma de la tortuga
frank.shapesize(2) ###Tamaño de la fugura
frank.pencolor("green") ###Color de la tortuga
frank.pensize(2) ##Grosor de la tortuga
def cuadrado():
    ##Emepezar a rellenar 
    frank.color("green", "blue") ###Primer argumento linea de color, segundo argumento Color de relleno
    frank.begin_fill()###Marcar inicio de relleno
    ###Creando un cuadrado
    frank.fd(100)
    frank.lt(90)
    frank.fd(100)
    frank.lt(90)
    frank.fd(100)
    frank.lt(90)
    frank.fd(100)
    frank.end_fill() ###fin de relleno
    input()

def triangulo():
    ##Emepezar a rellenar 
    frank.color("red") ###Primer argumento linea de color, segundo argumento Color de relleno
    frank.begin_fill()###Marcar inicio de relleno
    ###Creando un cuadrado
    frank.fd(100)
    frank.lt(120)
    frank.fd(100)
    frank.lt(120)
    frank.fd(100)
    frank.end_fill() ###fin de relleno
    input()

def pentagono():
    ##Emepezar a rellenar 
    frank.color("red") ###Primer argumento linea de color, segundo argumento Color de relleno
    frank.begin_fill()###Marcar inicio de relleno
    ###Creando un cuadrado
    frank.fd(100)
    frank.lt(360/5)
    frank.fd(100)
    frank.lt(360/5)
    frank.fd(100)
    frank.lt(360/5)
    frank.fd(100)
    frank.lt(360/5)
    frank.fd(100)
    frank.lt(360/5)        
    frank.end_fill() ###fin de relleno
    input()
#pentagono()
def hexagono():
    ##Emepezar a rellenar 
    frank.color("red") ###Primer argumento linea de color, segundo argumento Color de relleno
    frank.begin_fill()###Marcar inicio de relleno
    ###Creando un cuadrado
    frank.fd(100)
    frank.lt(360/6)
    frank.fd(100)
    frank.lt(360/6)
    frank.fd(100)
    frank.lt(360/6)
    frank.fd(100)
    frank.lt(360/6)
    frank.fd(100)
    frank.lt(360/6)
    frank.fd(100)
    frank.lt(360/6)
    frank.end_fill() ###fin de relleno
    input()
hexagono()
```

