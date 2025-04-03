from turtle import *
screensize(2000, 2000)
tracer(0)
k = 10
left(90)
begin_fill()
for i in range(9):
    forward(7 * k)
    right(90)
    forward(42 * k)
    right(90)
up()
back(10 * k)
left(90)
back(16 * k)
down()
for i in range(9):
    forward(42 * k)
    right(90)
    forward(16 * k)
    right(90)
end_fill()
cnt = 0
canvas = getcanvas()
for x in range(-30, 100):
    for y in range(-40, 90):
        if canvas.find_overlapping(x * k, y * k, x * k, y * k) == ():
            cnt += 1
print(cnt)
done()