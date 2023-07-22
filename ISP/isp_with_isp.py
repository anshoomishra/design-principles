# Lets apply ISP here
from abc import ABC,abstractmethod

class Movable(ABC):
    @abstractmethod
    def go(self):
        pass
class Flyable(ABC):
    @abstractmethod
    def fly(self):
        pass


class Car(Movable):
    def go(self):
        print("Car in only moving now....")

class Aircraft(Movable,Flyable):
    def go(self):
        print("Aircraft is moving.....")
    def fly(self):
        print("Aircraft is flying.....")

if __name__ == "__main__":
    car = Car()
    car.go()
    aircraft = Aircraft()
    aircraft.go()
    aircraft.fly()