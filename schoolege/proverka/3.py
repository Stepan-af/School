from turtle import *
tracer(0)
k = 100
left(90)
begin_fill()
for i in range(15):
    for j in range(20):
        forward(40 * k)
        right(90)
    left(90)
end_fill()
canvas = getcanvas()
cnt = 0
for x in range(-100, 100):
    for y in range(-100, 100):
        if canvas.find_overlapping(x * k, y * k, x * k, y * k) == (5,):
            cnt += 1
print(cnt)
done()