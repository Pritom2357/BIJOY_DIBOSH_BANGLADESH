import turtle
green_bd = turtle.Turtle()
red_bd = turtle.Turtle()

green_bd.speed(1)
red_bd.speed(1)

green_bd.penup()
green_bd.forward(700)
green_bd.backward(700)
green_bd.pendown()

green_bd.color("black", "green")
red_bd.color("black", "red")

green_bd.penup()
green_bd.setpos(-250, 0)
green_bd.pendown()

green_bd.begin_fill()

green_bd.forward(500)
green_bd.left(90)
green_bd.forward(200)
green_bd.left(90)
green_bd.forward(500)
green_bd.left(90)
green_bd.forward(200)
green_bd.left(90)

green_bd.end_fill()

red_bd.begin_fill()

red_bd.penup()
red_bd.setpos(0, 50)
red_bd.pendown()

red_bd.circle(60)

red_bd.end_fill()

turtle.exitonclick()
