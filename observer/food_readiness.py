from Factory.factory_with_factory import BurgerFactory,Burger
from abc import ABC,abstractmethod
class Kitchen:
    def __init__(self,name):
        self.name = name
        self.subscriber = []

    def notify(self):
        for sub in self.subscriber:
            sub.send_notification(sub.name)

    def subscribe(self,sub):
        self.subscriber.append(sub)

    def prepare_food(self,food):
        burger = BurgerFactory() \
            .add_patty("Cheese patty") \
            .add_veg("Veggie stuff") \
            .build()
        burger.build()
        return burger


class Subscriber(ABC):
    @abstractmethod
    def send_notification(self):
        pass

class KitchenSubscriber(Subscriber):
    def __init__(self,name):
        self.name = name

    def send_notification(self,name):
        print(f"Hi {name}, Your favorite food is ready now")

if __name__ == "__main__":

    kitchen = Kitchen("Food Hub")
    kitchen.subscribe(KitchenSubscriber("Anshu"))
    kitchen.subscribe(KitchenSubscriber("Sachin"))
    kitchen.notify()
