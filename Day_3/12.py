num = 0
salarySum = 0
salary = []
while True:
    s = input("input the salary:")
    if s.upper() == 'Q':
        print("done...")
        break
    if float(s) < 0:
        continue
    num += 1
    salarySum += float(s)
    salary.append(float(s))
print("the salary is:", salary)
print("{0} person have {1} in all".format(num, salarySum))
