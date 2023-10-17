class Burger:
    def __init__(self):
        self.patty = None
        self.cheese = None
        self.veg = None
        self.sauce = None

    def set_patty(self,patty):
        self.patty = patty

    def set_cheese(self, cheese):
        self.cheese = cheese

    def set_veg(self, veg):
        self.veg = veg

    def set_sauce(self, sauce):
        self.sauce = sauce

    def __str__(self):
        return "Your Burger contains " + self.patty + ", " + self.cheese + ", " + self.veg + ", " + self.sauce

class BurgerFactory:
    def __init__(self):
        self.burger = Burger()

    def add_patty(self,patty):
        self.burger.set_patty(patty)
        return self

    def add_cheese(self,cheese):
        self.burger.set_cheese(cheese)
        return self

    def add_veg(self,veg):
        self.burger.set_veg(veg)
        return self

    def add_sauce(self,sauce):
        self.burger.set_sauce(sauce)
        return self

    def build(self):
        return self.burger

if __name__ == "__main__":
    burger = BurgerFactory() \
        .add_patty("Cheese Patty") \
        .add_veg("Salad") \
        .add_sauce("Ketchup") \
        .add_cheese("Extra cheese") \
        .build()
    print(burger)