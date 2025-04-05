from turtle import*
k = 20
tracer(0)
screensize(1000, 1000)
left(90)
right(270)
for i in range(2):
    forward(8 * k)
    right(120)
right(120)
for i in range(2):
    right(120)
    forward(3 * k)
    right(240)
right(240)
for i in range(2):
    forward(14 * k)
    right(120)
up()
for x in range(-50, 70):
    for y in range(-50, 70):
        goto(x * k, y * k)
        dot(4, "red")
done()