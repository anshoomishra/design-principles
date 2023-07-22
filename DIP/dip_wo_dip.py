# Dependancy inversion principle ensures - High level code should not directly depend up low level module
# Here we can not integrate more appliance with switch
class Fan:
    def on(self):
        print("Fan is on now.....")
    def off(self):
        print("Fan is off now.....")    

class Switch:
    def __init__(self,fan:Fan):
        self.status = False
        self.fan = fan
    def press(self):
        if self.status:
            self.fan.off()
            self.status = False
        else:
            self.status = True
            self.fan.on()
if __name__ == "__main__":
    sw = Switch(Fan())
    sw.press()
    sw.press()