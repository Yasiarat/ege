from turtle import*

t = Turtle()
t.left(90)

size = 30
for i in range(4):
    t.forward(12 * size)
    t.right(90)

t.up()
for x in range(15):
    for y in range(15):
        t.goto(x * size, y * size)
        t.dot(5)

exitonclick()