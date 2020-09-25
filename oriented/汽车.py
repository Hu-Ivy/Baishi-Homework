class Car:
    def __init__(self, motor, chassis, seat, shell):
        self.motor = motor
        self.chassis = chassis
        self.seat = seat
        self.shell = shell

    def run(self):
        self.motor.work()
        self.seat.work()
        self.chassis.work()


class Motor:
    def work(self):
        print("Motor is work.")


class Seat:
    def work(self):
        print("seat is work...")


class Chassis:
    def work(self):
        print("chasis is work...")


class shell:
    pass
