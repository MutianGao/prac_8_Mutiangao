import random


class Car:
    def __init__(self, name='', fuel=0, reliability=0):
        self.name = name
        self.fuel = fuel
        self.reliability = reliability
        self.odometer = 0

    def __str__(self):
        return "Car:{}, fuel:{}, odometer:{}".format(self.name, self.fuel, self.odometer)

    def add_fuel_number(self, number):
        self.fuel = self.fuel + number

    def drive(self, dis_number):
        if random.randint(0, 100) > self.reliability:
            if dis_number > self.fuel:
                dis_number = self.fuel
                self.fuel = 0
            else:
                self.fuel = self.fuel - dis_number
            self.odometer = self.odometer + dis_number
            return dis_number
        else:
            dis_number = 0
            return dis_number
