'''
from turtle import*
left(90)
speed(0)
side = 20

for k in range(6):
    forward(10 * side)
    right(60)

up()
goto(0 * side, -5 * side)

for x in range(0, 30):
    for y in range(-5, 30):
        goto(x * side, y * side)
        dot(5)

mainloop()'''

'''from turtle import * # Подключим модуль черепашка
color('black','red') # устанавливаем цвет пера и цвет заливки
speed(100)
lt(90)
k = 20 # коэффициент для настраивания более удобного масштаба
begin_fill()
for i in range(12): #указываем число циклов необходимое до полного завершения фигуры
    rt(60)
    fd(2*k)
    rt(60)
    fd(2*k)
    rt(270)
end_fill()
cnt = 0
canvas = getcanvas()
for x in range(-100*k,100*k,k):
    for y in range(-100*k,100*k,k):
        s = canvas.find_overlapping(x,y,x,y)
        if len(s) == 1 and s[0] == 5:
            cnt+=1
print(cnt)
done()
exit()'''
from turtle import*
left(90)
speed(0)
tracer(1)
side = 30
c = 0
color('black', 'green')
begin_fill()
for i in range(8):
    forward(6 * side)
    right(120)

end_fill()
up()
can = getcanvas()
for x in range(0, 6 * side, side):
    for y in range(-3 * side, 7 * side, side):
        s = can.find_overlapping(x, -y, x, -y)
        goto(x, y)
        if 4 in s:
            color('yellow')
        elif 5 in s:
            color('red')
            c += 1

        else:
            color('blue')
        dot(3)
        print(s)
print(c)
mainloop()




















