from turtle import *
speed(1000)
m = 10
for i in range(9):
    forward(22 * m)
    right(90)
    forward(6 * m)
    right(90)
# up()
# forward(1 * m)
# right(90)
# forward(5 * m)
# left(90)
# down()
# for i in range(9):
#     forward(53 * m)
#     right(90)
#     forward(75 * m)
#     right(90)
up()
for x in range(-100, 100):
    for y in range(-100, 100):
        dot(10, "red")
        goto(x * m, y * m)
done()