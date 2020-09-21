sum_all = 0
sum_even = 0
sum_odd = 0
for num in range(101):
    if num % 2 == 0:
        sum_even += num
    else:
        sum_odd += num
    sum_all += num
print(sum_all)
print(sum_even)
print(sum_odd)
