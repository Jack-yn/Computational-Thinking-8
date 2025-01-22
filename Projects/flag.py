import turtle
t = turtle.Turtle()

# setup
t.speed(0)
turtle.Screen().bgcolor("light blue")


# stripes

# move to stripe 1
t.penup()
t.goto(-250, -100)
t.pendown()

height = 7.7

# stripe 1
t.color("red")
t.begin_fill()
t.forward(190)
t.left(90)
t.forward(height)
t.left(90)
t.forward(190)
t.left(90)
t.forward(height)
t.left(90)
t.end_fill()


# move to stripe 2
t.goto(-250, -92.3)

# stripe 2
t.color("white")
t.begin_fill()
t.forward(190)
t.left(90)
t.forward(height)
t.left(90)
t.forward(190)
t.left(90)
t.forward(height)
t.left(90)
t.end_fill()

# move to stripe 1
t.goto(-250, -84.6)

# stripe 1
t.color("red")
t.begin_fill()
t.forward(190)
t.left(90)
t.forward(height)
t.left(90)
t.forward(190)
t.left(90)
t.forward(height)
t.left(90)
t.end_fill()


# move to stripe 2
t.goto(-250, -76.9)

# stripe 2
t.color("white")
t.begin_fill()
t.forward(190)
t.left(90)
t.forward(height)
t.left(90)
t.forward(190)
t.left(90)
t.forward(height)
t.left(90)
t.end_fill()

# move to stripe 1
t.goto(-250, -69.2)

# stripe 1
t.color("red")
t.begin_fill()
t.forward(190)
t.left(90)
t.forward(height)
t.left(90)
t.forward(190)
t.left(90)
t.forward(height)
t.left(90)
t.end_fill()


# move to stripe 2
t.goto(-250, -61.5)

# stripe 2
t.color("white")
t.begin_fill()
t.forward(190)
t.left(90)
t.forward(height)
t.left(90)
t.forward(190)
t.left(90)
t.forward(height)
t.left(90)
t.end_fill()

# move to stripe 3
t.goto(-250, -53.8)

# stripe 3
t.color("red")
t.begin_fill()
t.forward(190)
t.left(90)
t.forward(height)
t.left(90)
t.forward(190)
t.left(90)
t.forward(height)
t.left(90)
t.end_fill()

# move to stripe 4
t.goto(-250, -46.1)

# stripe 4
t.color("white")
t.begin_fill()
t.forward(190)
t.left(90)
t.forward(height)
t.left(90)
t.forward(190)
t.left(90)
t.forward(height)
t.left(90)
t.end_fill()

# move to stripe 5
t.goto(-250, -38.4)

# stripe 5
t.color("red")
t.begin_fill()
t.forward(190)
t.left(90)
t.forward(height)
t.left(90)
t.forward(190)
t.left(90)
t.forward(height)
t.left(90)
t.end_fill()

# move to stripe 1
t.goto(-250, -30.7)

# stripe 1
t.color("white")
t.begin_fill()
t.forward(190)
t.left(90)
t.forward(height)
t.left(90)
t.forward(190)
t.left(90)
t.forward(height)
t.left(90)
t.end_fill()

# move to stripe 2
t.goto(-250, -23)

# stripe 2
t.color("red")
t.begin_fill()
t.forward(190)
t.left(90)
t.forward(height)
t.left(90)
t.forward(190)
t.left(90)
t.forward(height)
t.left(90)
t.end_fill()

# move to stripe 1
t.goto(-250, -15.3)

# stripe 1
t.color("white")
t.begin_fill()
t.forward(190)
t.left(90)
t.forward(height)
t.left(90)
t.forward(190)
t.left(90)
t.forward(height)
t.left(90)
t.end_fill()

# move to stripe 1
t.goto(-250, -7.6)

# stripe 1
t.color("red")
t.begin_fill()
t.forward(190)
t.left(90)
t.forward(height)
t.left(90)
t.forward(190)
t.left(90)
t.forward(height)
t.left(90)
t.end_fill()

# move to stripe 2
t.goto(-250, -50)

# blue square
t.goto(-250, -54)
t.color("darkblue")
t.begin_fill()
t.forward(76)
t.left(90)
t.forward(54)
t.left(90)
t.forward(76)
t.left(90)
t.forward(54)
t.left(90)
t.end_fill()

turtle.exitonclick()
