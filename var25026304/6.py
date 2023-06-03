from turtle import *

tracer(0, 0)
z = 20
left(90)
right(315)
for i in range(7):
    forward(12 * z)
    right(45)
    forward(6 * z)
    right(135)

pu()
for x in range(-10, 2):
    for y in range(0, 20):
        goto(x * z, y * z)
        dot(3)
update()
done()