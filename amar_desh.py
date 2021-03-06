import turtle
import time
head = turtle.Turtle()
bodyL= turtle.Turtle()
bodyR= turtle.Turtle()
legL = turtle.Turtle()
legR = turtle.Turtle()
handL= turtle.Turtle()
handR= turtle.Turtle()
flag = turtle.Turtle()
handle = turtle.Turtle()
circle = turtle.Turtle()
eye1 = turtle.Turtle()
eye2 = turtle.Turtle()
mouth = turtle.Turtle()

head.penup()
head.fd(4000)
head.setpos(0, 0)
head.pendown()

head.speed(1)
bodyL.speed(1)
bodyR.speed(1)
legL.speed(1)
legR.speed(1)
handL.speed(1)
handR.speed(1)
handle.speed(1)
circle.speed(1)
eye1.speed(1)
eye2.speed(1)
mouth.speed(1)

head.color('black', '#F6DDCC')
bodyL.color('black', '#5DADE2')
bodyR.color('black', '#5DADE2')
legL.color('black', '#273746')
legR.color('black', '#273746')
handL.color('black','#F6DDCC')
handR.color('black', '#F6DDCC')
flag.color('black', '#1E8449')
handle.color('black', '#A04000')
circle.color('black', '#FF0000')
eye1.color('black', '#EEEEEE')
eye2.color('black', '#EEEEEE')
mouth.color('black')

head.begin_fill()
head.circle(50)
head.ht()
head.end_fill()

mouth.begin_fill()
mouth.penup()
mouth.setpos(20, 30)
mouth.pendown()
mouth.right(90)
mouth.circle(-20, 180)
mouth.ht()
mouth.end_fill()

eye1.begin_fill()
eye2.begin_fill()
eye1.penup()
eye2.penup()
eye1.setpos(20, 60)
eye2.setpos(-20, 60)
eye1.pendown()
eye2.pendown()
eye1.circle(9)
eye2.circle(9)
eye1.ht()
eye2.ht()
eye1.end_fill()
eye2.end_fill()

bodyL.begin_fill()
bodyR.begin_fill()
bodyL.penup()
bodyR.penup()
handL.penup()
handR.penup()
bodyL.setpos(-30, 10)
bodyR.setpos(30, 10)
handL.setpos(-30, 10)
handR.setpos(30, 10)
bodyL.left(220)
bodyR.right(50)
handL.left(220)
handR.right(50)
handL.fd(75)
handR.fd(75)
handL.left(90)
handR.right(90)
bodyL.pendown()
bodyR.pendown()
handL.pendown()
handR.pendown()

bodyL.fd(75)
bodyR.fd(75)
bodyL.left(90)
bodyR.right(90)
bodyL.fd(35)
bodyR.fd(35)
bodyL.left(100)
bodyR.right(100)
bodyL.fd(45)
bodyR.fd(45)
bodyR.left(145)
bodyL.right(135)
bodyL.fd(115)
bodyR.fd(120)
bodyL.right(275)
bodyL.fd(50)
bodyL.ht()
bodyR.ht()
bodyL.end_fill()
bodyR.end_fill()

handL.begin_fill()
handR.begin_fill()
handL.fd(5)
handR.fd(5)
handL.right(90)
handR.left(60)
handL.fd(50)
handR.fd(50)
handL.right(30)
handR.right(10)
handL.fd(100)
handR.fd(75)
handL.circle(10, 180)
handR.circle(-10, 180)
handL.right(2)
handR.left(2)
handL.fd(110)
handR.fd(80)
handL.left(30)
handR.left(10)
handL.fd(60)
handR.fd(35)
handL.ht()
handR.ht()
handL.end_fill()
handR.end_fill()


legL.penup()
legR.penup()
legL.setpos(-25, -145)
legR.setpos(20, -145)
legL.pendown()
legR.pendown()

legL.begin_fill()
legR.begin_fill()
legL.right(100)
legR.right(80)
legL.fd(150)
legR.fd(150)
legL.right(10)
legR.left(10)
legL.fd(20)
legR.fd(20)
legL.circle(10, 180)
legR.circle(-10, 180)
legL.fd(20)
legR.fd(20)
legR.right(7)
legL.left(7)
legL.fd(160)
legR.fd(160)
legL.ht()
legR.ht()
legL.end_fill()
legR.end_fill()

handle.begin_fill()
handle.penup()
handle.setpos(-200, -315)
handle.pendown()

handle.left(90)
handle.fd(550)
handle.left(90)
handle.fd(7)
handle.left(90)
handle.fd(550)
handle.left(90)
handle.fd(7)
handle.ht()
handle.end_fill()

flag.begin_fill()
flag.penup()
flag.setpos(-200, 100)
flag.pendown()

flag.fd(300)
flag.left(90)
flag.fd(125)
flag.left(90)
flag.fd(300)
flag.left(90)
flag.fd(125)
flag.left(90)
flag.ht()
flag.end_fill()

circle.begin_fill()
circle.penup()
circle.setpos(-50, 120)
circle.pendown()

circle.circle(40)
circle.ht()
circle.end_fill()

turtle.exitonclick()
