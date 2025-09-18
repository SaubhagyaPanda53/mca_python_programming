from turtle import *
speed('fast')
side = 7
for i in range(side):
    for i in range (side-1):
        for i in range(side-1):
            fd(25)
            lt(360/side-1)
    fd(100)
    lt(360/side)

hideturtle()
mainloop()
