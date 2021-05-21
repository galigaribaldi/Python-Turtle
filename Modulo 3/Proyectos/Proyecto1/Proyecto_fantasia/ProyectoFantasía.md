# Proyecto Opcional Módulo 3 *Fantasía*

Este proyecto es meramente opcional y no es necesario realziarlo si no se desean puntos extras

Este se debe de recrear con ayuda del lenguaje de programación Python y la librería [Turtle](https://docs.python.org/3/library/turtle.html#turtle.write) y  debe de contener las características que se describen a continuación

## Especificaciones Generales

Formato de entrega, se debe entregar 2 archivos:

1. **Código del programa:** Guardar el código con el nombre *proyecto-tablero.py*

2. **Reporte del código:** Este debe conllevar los siguientes puntos:

   1. Nombre del alumno

   2. Fecha

   3. Nombre del proyecto

   4. Problemática que se soluciona

   5. Código realizado por el alumno

      ```python
      """
      @author: nombre de quien hace el programa
      @date: Fecha en la que se realiza el programa
      @description: Descripcion del programa
      """
      Completar el código de la actividad que se realiza
      ```

   6. Captura de pantalla del código ejecutandose

   7. Captura de pantalla del validador (En este proyecto no hay validador, este punto se omite)

## Especificaciones del código 

Para este proyecto no se calificarán calidad ni métodos de programación, sólo se calfiicará el resultado final del dibujo. Sin embargo se calificarán como extra los siguientes puntos:

1. **<u>Función creadora de una figura primaria:</u>** Función generadora de una figura base para la creación de dibujos, éste puede ser un cuadrado, triángulo, etc.

   ```python
   ##Funcion creadora de Figura
   def cuadrado(tam):
       for _ in range(_):
           frank.forward(tam)
           frank.right(90)   
   ```

2. **<u>Colores:</u>** Se calificarán colores usados en el código, éstos meramente pondrán serán visuales y se pueden usar los colores que se deseen

   ```python
   color(Color1,Color2)
   frank.begin_fill()
   figura(tam)
   frank.end_fill()
   ```

3. **Creatividad:** Para este proyecto se calificará la creatividad, por lo que hacer un dibujo propio se le podrá subir hasta 2 puntos extras

4. **Sugerencias:** Se adjuntan algunos códigos de ejemplo, estos se encuentran incompletos y se dejan de tarea completarlos.

   **Among US**
   
   ```python
   def jiu():
       t.pensize(20)
   
       t.fillcolor(color1)
       t.begin_fill()
   
       t.right(90)
       t.forward(50)
       t.right(180)
       t.circle(40, -180)
       t.right(180)
       t.forward(200)
   
       t.right(180)
       t.circle(100, -180)
   
       t.backward(20)
       t.left(15)
       t.circle(500, -20)
       t.backward(20)
   
       t.circle(40, -180)
       t.left(7)
       t.backward(50)
   
       t.up()
       t.left(90)
       t.forward(10)
       t.right(90)
       t.down()
   
       t.right(240)
       t.circle(50, -70)
   
       t.end_fill()
   
   
   def glass():
       t.up()
   
       t.right(230)
       t.forward(100)
       t.left(90)
       t.forward(20)
       t.right(90)
   
       t.down()
       t.fillcolor(color3)
       t.begin_fill()
   
       t.right(150)
       t.circle(90, -55)
   
       t.right(180)
       t.forward(1)
       t.right(180)
       t.circle(10, -65)
       t.right(180)
       t.forward(110)
       t.right(180)
       
       t.circle(50, -190)
       t.right(170)
       t.forward(80)
   
       t.right(180)
       t.circle(45, -30)
   
       t.end_fill()
   ```

Ejecución y demostración del programa

<img src="../../../../../../Library/Application Support/typora-user-images/image-20210521012352453.png" alt="image-20210521012352453" style="zoom:50%;" />

**Sharingan**

```python
def circulo_interno(tam):
    frank.rt(180) 
    frank.begin_fill()
    frank.circle(tam)
    frank.end_fill()    
    frank.rt(70)
    ###
    if tam > 50:
        frank.pensize(30)
    else:
        frank.pensize(10)
    frank.circle(tam-5,100)
    frank.penup()
    frank.circle(tam-5,260)
    frank.lt(90)
    frank.fd(tam/3)
    frank.rt(90)
    frank.pendown()
    frank.circle(tam,80)
    frank.penup()
    frank.circle(tam,280)
    frank.pendown()
    frank.pensize(1)
    frank.rt(110)

def triangulo(tam):
    for _ in range(3):
        frank.lt(360/3)
        frank.penup()
        frank.forward(tam)
        frank.pendown()
        frank.color("black","black")
        frank.begin_fill()
        circulo_interno(20)
        frank.end_fill()
```

<img src="../../../../../../Library/Application Support/typora-user-images/image-20210521012552394.png" alt="image-20210521012552394" style="zoom:50%;" />

**Mandala 1**

```python
def draw_art():
    frank = Turtle(shape="turtle")
    frank.color("yellow")
    frank.pensize(2)
    frank.speed(0)
    for _ in range(36):
        draw_square(frank)
        frank.rt(10)
    ## Turtle Angie
    angie = Turtle(shape="turtle")
    angie.color("blue")
    angie.pensize(2)
    angie.speed(0)
    size = 1
    for _ in range(300):
        angie.forward(size)
        angie.right(91)
        size += 1
```

<img src="../../../../../../Library/Application Support/typora-user-images/image-20210521012820141.png" alt="image-20210521012820141" style="zoom:50%;" />

## Extras

Esta sección detalla los puntos extra que el programa puede tener

- **Color de pantalla de fondo:** Proponer e implementar un color diferente a la pantalla blanca. *TIP: Usar el screen de turtle*
- **Color de Tortuga y forma de la tortuga:** Proponer un color y forma de la tortuga 
