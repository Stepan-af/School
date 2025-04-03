from turtle import *
screensize(1000, 1000)
tracer(0)
k = 100
left(90)
right(45)
begin_fill()
for i in range(7):
    forward(6 * k)
    right(45)
    forward(12 * k)
    right(135)
end_fill()
cnt = 0
canvas = getcanvas()
for x in range(-100, 100):
    for y in range(-100, 100):
        if canvas.find_overlapping(x * k, y * k, x * k, y * k) == (5,):
            cnt += 1
print(cnt)
done()