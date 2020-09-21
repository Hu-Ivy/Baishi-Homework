x = input("input x,y:")
y = input("input x,y:")

if (x == 0 and y == 0):
    print("原点")
elif (x == 0):
    print("x轴")
elif (y == 0):
    print("y轴")
elif (x > 0 and y > 0):
    print("第一象限")
elif (x > 0 and y < 0):
    print("第二象限")
elif (x < 0 and y > 0):
    print("第三象限")
elif (x < 0 and y < 0):
    print("第四象限")
