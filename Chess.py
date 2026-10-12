import turtle
tom = turtle.Turtle()

screen = turtle.Screen()
width = screen.window_width()
height = screen.window_height()

board_size = min(width, height) * 0.8
STEP = board_size / 8

label_offset = STEP*0.7
font_size = max(8, int(STEP*0.2))

tom.hideturtle()
turtle.tracer(0, 0)
tom.speed(10)
tom.pensize(2)

tom.penup
tom.goto(-(board_size/2), -(board_size/2))
tom.pendown()
tom.left(90)

for i in range(4):
    tom.forward(board_size)
    tom.right(90)

tom.penup()
tom.goto(-(board_size/2), -(board_size/2))
tom.setheading(0)
tom.pendown()

def green_square():
    for i in range(4):
        tom.fillcolor("green")
        tom.begin_fill()
        for i in range(4):
            tom.forward(STEP)
            tom.left(90)
        tom.end_fill()
        tom.forward(STEP*2)
    tom.backward(board_size)
    tom.left(90)
    tom.forward(STEP)
    tom.right(90) #If code doesn't work recheck here.
    tom.forward(STEP)
    tom.fillcolor("green")
    tom.begin_fill()
    for i in range(3):
        tom.forward(STEP)
        tom.left(90)
        tom.forward(STEP)
        tom.left(90)
        tom.forward(STEP)
        tom.left(90)
        tom.forward(STEP)
        tom.left(90)
        tom.forward(STEP*2)
    tom.end_fill()
    tom.fillcolor("green")
    tom.begin_fill()
    for i in range(4):
        tom.forward(STEP)
        tom.left(90)
    tom.end_fill()
    tom.backward(STEP*7)
    tom.left(90)
    tom.forward(STEP)
    tom.right(90)

for i in range(4):
    green_square()

x = (board_size/2) - (STEP/2)
y = -(board_size/2) - label_offset

for i in range(104, 96, -1):
    tom.penup()
    tom.goto(x, y)
    files = chr(i)
    tom.write(files, move=False, align="center", font=("Arial", font_size, "normal"))
    x = x-STEP

x = -(board_size/2) - label_offset
y = -(board_size/2) + (STEP/2)
tom.penup()
tom.goto(x, y)

for i in range(1,9,1):
    tom.pendown()
    tom.write(i, move=False, align="center", font=("Arial", font_size, "normal"))
    tom.penup()
    y = y+STEP
    tom.goto(x, y)

x = -(board_size/2) + (STEP/2)
y = (board_size/2) +(label_offset/2)
tom.penup()
tom.goto(x, y)

for i in range(97,105,1):
    files=chr(i)
    tom.pendown()
    tom.write(files, move=False, align="center", font=("Arial", font_size, "normal"))
    x = x+STEP
    tom.penup()
    tom.goto(x, y)

x=(board_size/2) + label_offset
y = (board_size/2) - (STEP/2)
tom.penup()
tom.goto(x, y)

for i in range(8,0,-1):
    tom.pendown()
    tom.write(i, move=False, align="center", font=("Arial", font_size, "normal"))
    tom.penup()
    y = y-STEP
    tom.goto(x, y)



turtle.update()
turtle.done()