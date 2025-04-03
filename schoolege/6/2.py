from turtle import *
tracer(0)
k = 20
down()
for i in range(9):
    forward(22 * k)
    right(90)
    forward(6 * k)
    right(90)
up()
forward(1 * k)
right(90)
forward(5 * k)
left(90)
down()
for i in range(9):
    forward(53 * k)
    right(90)
    forward(75 * k)
    right(90)
up()
for x in range(-100, 100):
    for y in range(-100, 100):
        dot(4, 'red')
        goto(x * k, y * k)
done()