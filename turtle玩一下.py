import turtle

def sierpinski(turtle, length, level):
    if level == 0:
        triangle(turtle, length)

    else:

        curpos = t.position()  # 保留起始点坐标

        length *= 0.5

        sierpinski(turtle, length, level - 1)

        turtle.penup()

        turtle.forward(length)

        turtle.pendown()

        sierpinski(turtle, length, level - 1)

        turtle.penup()

        turtle.left(120)

        turtle.forward(length)

        turtle.right(120)

        turtle.pendown()

        sierpinski(turtle, length, level - 1)

        t.setposition(curpos[0], curpos[1])  # 回到起始点，方向也复原


def triangle(t, length):
    for i in range(3):
        t.forward(length)

        t.left(120)


scr = turtle.Screen()

t = turtle.Pen()  # 初始化乌龟程序，调出图形框，准备好画笔

t.shape("turtle")  # 改变画笔形状为一只乌龟，缺省是箭头arrow，

# 还可以为 'circle'-圆, 'square'-正方形, 'triangle'-三角形, 'classic'.


scr.bgcolor("white")  # (0.1,0.51,0.3)   # red,green,blue 取值在0和1之间。1代表255,

t.pensize(2)  # 改变线宽度

t.color("green")  # 改变画笔颜色,还有green,blue,black,white,pink,...,或者(r,g,b)

t.speed(0)

t.penup()

t.setposition(-200, -100)

t.pendown()

sierpinski(t, 400, 4)

t.hideturtle()  # 隐藏乌龟图形

scr.exitonclick()
