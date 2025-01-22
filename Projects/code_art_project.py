#imports

import turtle

#setup

t = turtle.Turtle()
t.penup()
t.goto(-100, 0)
t.color("black")
t.pendown()
t.speed(0)
t.strokeWidth={1}

#shape maki

colors = ["black", "lightblue"]
for i in range(900):
    t.color( colors[i % 2 ])
    t.forward(200 + i)
    t.left(179.8)


#ending

turtle.exitonclick()