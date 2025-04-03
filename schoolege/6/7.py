from turtle import *
tracer(0)
screensize(1000, 1000)
k = 20
left(90)
for i in range(2):
    forward(21 * k)
    right(90)
    forward(27 * k)
    right(90)
up()
forward(9 * k)
right(90)
forward(10 * k)
left(90)
down()
for i in range(2):
    forward(86 * k)
    right(90)
    forward(47 * k)
    right(90)
up()
for x in range(-20, 110):
    for y in range(-20, 110):
        goto(x * k, y * k)
        dot(4)
done()