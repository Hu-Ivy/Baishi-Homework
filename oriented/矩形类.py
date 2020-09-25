class MyRectangle():
    def __init__(self, x=0, y=0, width=100, height=100):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def getArea(self):
        return self.width * self.height;

    def getPerimeter(self):
        return (self.width + self.height) * 2

    def draw(self):
        import turtle
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.pendown()
        turtle.goto((self.x + self.width, self.y))
        turtle.goto((self.x + self.width, self.y + self.height))
        turtle.goto((self.x, self.y + self.height))
        turtle.goto((self.x, self.y))
        turtle.done()
s=MyRectangle()
s.draw()