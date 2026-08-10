!pip install ColabTurtlePlus
import ColabTurtlePlus.Turtle as turtle

import ColabTurtlePlus.Turtle as turtle

# Crear la ventana
pantalla = turtle.Screen()
pantalla.bgcolor("white")
turtle.clearscreen()

# Crear la tortuga 1
t1 = turtle.Turtle()
t1.shape("turtle")
t1.color("blue")
t1.pensize(4)
t1.speed(13)
t1.clear()
t1.penup()
t1.goto(-300,0)


# Crear la tortuga 2
t2 = turtle.Turtle()
t2.shape("turtle")
t2.color("red")
t2.pensize(4)
t2.speed(13)
t2.clear()
t2.penup()
t2.goto(-300,100)

# Crear la tortuga 3
t3 = turtle.Turtle()
t3.shape("turtle")
t3.color("green")
t3.pensize(4)
t3.speed(13)
t3.clear()
t3.penup()
t3.goto(-300,200)

# Crear la tortuga 4
t4 = turtle.Turtle()
t4.shape("turtle")
t4.color("black")
t4.pensize(4)
t4.speed(13)
t4.clear()
t4.penup()
t4.goto(-300,-100)
# Crear la tortuga 5
t5 = turtle.Turtle()
t5.shape("turtle")
t5.color("orange")
t5.pensize(4)
t5.speed(13)
t5.clear()
t5.penup()
t5.goto(-300,-200)

# reajustar velosidad
t1.speed(5)
t2.speed(3)
t3.speed(1)
t4.speed(4)
t5.speed(7)

# Carrera
for i in range(25):
  t1.forward(15)
  t2.forward(10)
  t3.forward(5)
  t4.forward(12)
  t5.forward(17)

for i in range(12):
  t2.forward(14.5)
  t3.forward(25)
  t1.forward(4.1)
  t4.forward(10)