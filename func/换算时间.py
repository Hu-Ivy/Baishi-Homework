def change_time():
    mseconds = int(input("input mseconds:"))
    seconds = mseconds / 1000
    minute = seconds / 60
    hours = minute / 60
    print("相当于{0}小时{1}分钟{2}秒".format(hours, minute, seconds))


change_time()
