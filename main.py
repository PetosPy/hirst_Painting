
from turtle import Turtle, Screen
import turtle as t
import random
t.colormode(255)

screen = Screen()
screen.title("Hirst Painting")

#R,G,B color creater, works together with colormode.
def color_maker():
    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)
    color = (r, g, b)
    return color


pet = Turtle()
pet.penup()
pet.hideturtle()
pet.speed("fastest")
pet.setheading(225)
pet.forward(300)
pet.setheading(0)


#pet.pencolor(color_maker())

game_on = 10

while game_on > 0:
    for _ in range(10):
        pet.dot(30,color_maker())
        pet.forward(50)

    pet.left(90)
    pet.forward(50)
    pet.left(90)
    pet.forward(500)
    pet.setheading(0)
    game_on -= 1



screen.exitonclick()