class Employee:
    id = 1000

    def __init__(self, name, salary):

        self.id = Employee.id + 1
        self.name = name
        self.__salary = salary
        Employee.id += 1

    def __add__(self, other):
        if isinstance(other, Employee):
            return other.salary + self.salary

    @property
    def salary(self):
        print("salary is {0}".format(self.__salary))

    @salary.setter
    def salary(self, salary):
        if (1000 < salary < 50000):
            self.__salary = salary
        else:
            print("input again")

print(dir(Employee))
e1 = Employee("a", 3000)

e2 = Employee("b", 2000)
e3 = Employee("b", 4000)
e3.salary = 5000
print(e1.id)
print(e2.id)
print(e3.id)
print(e3.salary)
