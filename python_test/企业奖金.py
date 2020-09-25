def bonus():
    benifit = float(input("输入利润"))
    l = [0.1, 0.075, 0.05, 0.03, 1.5, 0.01]
    b1 = 100000 * l[0]
    b2 = 100000 * l[1]
    b3 = 200000 * l[2]
    b4 = 200000 * l[3]
    b5 = 400000 * l[4]
    if benifit <= 100000:
        return benifit * l[0]
    elif benifit <= 200000:
        return b1 + (benifit - 100000) * l[1]
    elif benifit <= 400000:
        return b1 + b2 + (benifit - 200000) * l[2]
    elif benifit <= 600000:
        return b1 + b2 + b3 + (benifit - 400000) * l[3]
    elif benifit <= 1000000:
        return b1 + b2 + b3 + b4 + (benifit - 600000) * l[4]
    else:
        return b1 + b2 + b3 + b4 + b5 + (benifit - 1000000) * l[5]


print(bonus())
