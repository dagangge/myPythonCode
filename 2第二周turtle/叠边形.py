import turtle
turtle.setup(600,500)
turtle.penup()
turtle.goto(-100,-100)
turtle.pendown()
turtle.pensize(15)
turtle.pencolor("black")
for x in range(9):
    turtle.fd(200)
    turtle.left(80)
turtle.done()