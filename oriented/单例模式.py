class ComputerFactory:
    __obj = None
    __init_flag = True

    def create_car(self, brand):
        if brand == '华硕':
            return Huashuo()
        elif brand == '联想':
            return Lianxiang()
        elif brand == '神州':
            return Shenzhou()
        else:
            return "未知品牌无法创建"

    def __new__(cls, *args, **kwargs):
        if cls.__obj == None:
            cls.__obj = object.__new__()
        return cls.__obj

    def __init__(self):
        if ComputerFactory.__init_flag:
            print("init computerfactory")
            ComputerFactory.__init_flag = False

class Computer:
    def calculate(self):
        print("calculate computer")

class Lianxiang(Computer):
    def calculate(self):
        print("calculate Lianxiang")


class Huashuo(Computer):
    def calculate(self):
        print("calculate Huashuo")


class Shenzhou(Computer):
    def calculate(self):
        print("calculate Shenzhou")
