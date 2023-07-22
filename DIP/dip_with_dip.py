from abc import ABC
class Switable(ABC):
    def on(self):
        pass
    def off(self):
        pass

class LightBulb(Switable):
    def on(self):
        print("Bulb is on now.......")
    def off(self):
        print("Bulb is off now.......")

class Fan(Switable):
    def on(self):
        print("Fan is on now.......")
    def off(self):
        print("Fan is off now.......")


class Switch():
    def __init__(self,appliance:Switable):
        self.status = False
        self.appliance = appliance
    
    def press(self):
        if self.status:
            self.appliance.off()
            self.status = False
        else:
            self.appliance.on()
            self.status = True


if __name__ == "__main__":
    fan = Fan()
    sw = Switch(fan)
    sw.press()
    sw.press()