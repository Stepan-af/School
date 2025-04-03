from turtle import *
screensize(1000, 1000)
tracer(0)
k = 20
left(90)
for i in range(10):
    forward(22 * k)
    right(90)
    forward(16 * k)
    right(90)
up()
forward(1 * k)
right(90)
forward(1 * k)
left(90)
down()
for i in range(10):
    forward(72 * k)
    right(90)
    forward(79 * k)
    right(90)
up()
for x in range(-100, 100):
    for y in range(-100, 100):
        goto(x * k, y * k)
        dot(4)
done()