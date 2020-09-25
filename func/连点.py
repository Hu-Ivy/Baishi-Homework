import turtle


def line_point():
    x = []
    while True:
        point = input("输入坐标用逗号隔开:")
        if point == 'q':
            break
        x.append(eval(point))
    print(x)
    n = len(x)
    t = turtle.Pen()
    t.speed(10)
    for i in range(n):
        for j in range(i,n):
            t.penup()
            t.goto(x[i])
            t.pendown()
            t.goto(x[j])

    turtle.done()
line_point()
