def baiqianmaiji(money, number):
    method = []
    for gongji in range(0, number+1):
        for muji in range(0, number - gongji+1):
            xiaoji = 100 - gongji*5 - muji*3
            if xiaoji>=0:
                method.append((gongji, muji, xiaoji))
    return len(method)


print(baiqianmaiji(100, 100))
