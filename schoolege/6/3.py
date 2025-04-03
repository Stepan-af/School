from turtle import *
speed(1000)
m = 30
begin_fill()
left(90)
for i in range(7):
    forward(10 * m)
    right(120)
end_fill()
canvas = getcanvas()
cnt = 0
for x in range(-200, 200):
    for y in range(-200, 200):
        if canvas.find_overlapping(x * m, y * m, x * m, y * m) == (5,):
            cnt += 1
print(cnt)
done()