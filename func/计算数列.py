def cal_array(n):
    if n==1:
        return 1/2
    return n/(n+1)+cal_array(n-1)
print(cal_array(2))