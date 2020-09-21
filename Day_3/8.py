for i in range(10):
    for j in range(i + 1):
        print("{0}*{1}={2}".format(i, j, i * j), end='\t')
    print()
