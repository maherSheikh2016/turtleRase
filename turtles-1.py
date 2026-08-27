import random
import tkinter as tk
import turtle
import time

# Crear la ventana
pantalla = turtle.Screen()
pantalla.colormode(255)
pantalla.bgcolor(144, 238, 144)

#dibujar la meta
meta = turtle.Turtle()
meta.shape("square")
meta.color("black")
meta.shapesize(0.5)
meta.penup()
meta.goto(320, 250)
meta.pensize(5)
meta.pendown()
meta.goto(320, -250)
meta.hideturtle()
meta.pencolor("white")
for i in range(6):
    meta.penup()
    meta.goto(320, 250 - (i * 100))
    meta.pendown()
    meta.goto(-300, 250 - (i * 100))

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
t5.color("yellow")
t5.pensize(4)
t5.speed(13)
t5.clear()
t5.penup()
t5.goto(-300,-200)

#semaforo
semaforo = turtle.Turtle()
semaforo.shape("circle")
colors = ["red", "yellow", "green"]
position = 200
semaforo.penup()
for color in colors:
  semaforo.color(color)
  semaforo.goto(0, position)
  position -= 50
  time.sleep(1)

semaforo.hideturtle()

# reajustar velosidad
t1.speed(4)
t2.speed(2)
t3.speed(1)
t4.speed(3)
t5.speed(6)

# Carrera
tortugas = {
    t1: "Tortuga Azul", 
    t2: "Tortuga Roja",
    t3: "Tortuga Verde",
    t4: "Tortuga Negra",
    t5: "Tortuga Amarilla"
}
winner = None

while not winner:
    for keys, values in tortugas.items():
        keys.forward(random.randint(1, 10))
        if keys.xcor() >= 300:
            winner = values
            root = tk.Tk()
            label = tk.Label(root, text=f"¡La {winner} ha ganado la carrera!")
            label.pack()
            break
turtle.done()