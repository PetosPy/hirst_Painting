
from turtle import Turtle, Screen
import turtle
import random
turtle.colormode(255)

color_list = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136),
              (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149),
              (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89),
              (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208)]



color_choice = random.choice(color_list)
pet = Turtle()
pet.penup()
pet.hideturtle()
pet.speed("fastest")
pet.setheading(225)
pet.forward(300)
pet.setheading(0)


pet.pencolor(color_choice)

game_on = 10

while game_on > 0:
    for _ in range(10):
        pet.dot(30, random.choice(color_list))
        pet.forward(50)

    pet.left(90)
    pet.forward(50)
    pet.left(90)
    pet.forward(500)
    pet.setheading(0)
    game_on -= 1


screen = Screen()
screen.exitonclick()