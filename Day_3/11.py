num = 0
salarySum = 0
salary = []
for i in range(4):
    s = input("input the salary:")

    if s.upper() == 'Q':
        print("done...")
        break
    if float(s) < 0:
        continue
    num += 1
    salarySum += float(s)
    salary.append(float(s))

else:
    print("input over")
    salaryAver = salarySum / 4
print("the salary is:", salary)
print("average salary is : {0}".format(salaryAver))
