from turtle import *
tracer(0)
screensize(1000, 1000)
k = 30
left(90)
for i in range(7):
    forward(10 * k)
    right(120)
up()
for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x * k, y * k)
        dot(4)
done()