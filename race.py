import random
import time
import tkinter as tk
import turtle


START_X = -300
FINISH_X = 300

TURTLE_CONFIG = (
    ("blue", 0, 4, "Tortuga Azul"),
    ("red", 100, 2, "Tortuga Roja"),
    ("green", 200, 1, "Tortuga Verde"),
    ("black", -100, 3, "Tortuga Negra"),
    ("yellow", -200, 6, "Tortuga Amarilla"),
)


def create_turtle(color, y_position, speed):
    racer = turtle.Turtle()
    racer.shape("turtle")
    racer.color(color)
    racer.pensize(4)
    racer.speed(speed)
    racer.penup()
    racer.goto(START_X, y_position)
    return racer


def create_racers():
    return {
        create_turtle(color, y_position, speed): name
        for color, y_position, speed, name in TURTLE_CONFIG
    }


def draw_finish_line():
    finish_line = turtle.Turtle()
    finish_line.shape("square")
    finish_line.color("black")
    finish_line.shapesize(0.5)
    finish_line.penup()
    finish_line.goto(FINISH_X + 20, 250)
    finish_line.pensize(5)
    finish_line.pendown()
    finish_line.goto(FINISH_X + 20, -250)
    finish_line.hideturtle()
    finish_line.pencolor("white")

    for row in range(6):
        y_position = 250 - row * 100
        finish_line.penup()
        finish_line.goto(FINISH_X + 20, y_position)
        finish_line.pendown()
        finish_line.goto(START_X, y_position)


def show_countdown():
    countdown = turtle.Turtle()
    countdown.shape("circle")
    countdown.penup()

    for color, y_position in zip(("red", "yellow", "green"), (200, 150, 100)):
        countdown.color(color)
        countdown.goto(0, y_position)
        time.sleep(1)

    countdown.hideturtle()


def show_winner(winner):
    root = tk.Tk()
    root.title("Carrera de tortugas")
    tk.Label(root, text=f"¡La {winner} ha ganado la carrera!").pack(padx=20, pady=20)
    root.mainloop()


def run_race(racers):
    while True:
        for racer, name in racers.items():
            racer.forward(random.randint(1, 10))
            if racer.xcor() >= FINISH_X:
                return name


def start_race():
    screen = turtle.Screen()
    screen.colormode(255)
    screen.bgcolor(144, 238, 144)
    draw_finish_line()
    racers = create_racers()
    show_countdown()
    winner = run_race(racers)
    show_winner(winner)
    turtle.done()