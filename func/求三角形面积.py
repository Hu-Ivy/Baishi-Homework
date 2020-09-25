from math import sqrt, fabs


def cal_area():
    point = input("please input the point:")
    x1 = float(point[0])
    y1 = float(point[1])
    x2 = float(point[2])
    y2 = float(point[3])
    x3 = float(point[4])
    y3 = float(point[5])
    a = sqrt(fabs(pow(y2 - y1, 2)) + fabs(pow(x2 - x1, 2)))
    b = sqrt(fabs(pow(y3 - y1, 2)) + fabs(pow(x3 - x1, 2)))
    c = sqrt(fabs(pow(y2 - y3, 2)) + fabs(pow(x2 - x3, 2)))
    p = (a + b + c) / 2
    if a == p or b == p or c == p:
        print("无效三角形")
    else:
        s = sqrt(p * (p - a) * (p - b) * (p - c))
        print("the area is {0}".format(s))


cal_area()
