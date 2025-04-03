from turtle import *
tracer(0)
k = 20
screensize(1920, 1080)
left(90)
for i in range(8):
    forward(16 * k)
    right(90)
    forward(22 * k)
    right(90)
up()
forward(5 * k)
right(90)
forward(5 * k)
left(90)
down()
for i in range(8):
    forward(52 * k)
    right(90)
    forward(77 * k)
    right(90)
up()
pencolor = 'red'
for x in range(0, 150):
    for y in range(0, 80):
        goto(x * k, y * k)
        dot(4)
        
done()