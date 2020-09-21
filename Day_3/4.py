score = int(input("input the score:"))
grade = ""

if score > 100 or score < 0:
    print("input again")
else:
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "E"
    print("score is {0}, level is {1}".format(score, grade))
