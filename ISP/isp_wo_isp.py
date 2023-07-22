# ISP principle ensures that interfaces must have unique responsibility
from abc import ABC,abstractmethod

class Vehicle(ABC):
    def go(self):
        pass
    def fly(self):
        pass

class Car(Vehicle):
    def go(self):
        print("Car is moving.....")
    #wrong implementation here
    def fly(self):
        print("Car should not fly.....")

class Aircraft(Vehicle):
    def go(self):
        print("Aircraft is moving.....")

    def fly(self):
        print("Aircraft flying.....")

if __name__ == "__main__":
    car = Car()
    car.go()
    #wrong here
    car.fly()