import turtle
turtle.setup(600,500)
turtle.penup()
turtle.seth(-90)
turtle.fd(160)
turtle.pendown()
turtle.pensize(20)
turtle.colormode(255)
for j in range(10):
    turtle.speed(1000)
    turtle.pencolor(25*j, 5*j,15*j)
    turtle.seth(130)
    turtle.fd(220)
    for i in range(23):
        turtle.circle(-80,10)
    turtle.seth(100)
    for i in range(23):
        turtle.circle(-80, 10)
    turtle.fd(220)
turtle.done()