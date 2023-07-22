# Here we are implementing OCP 
from abc import ABC,abstractmethod
class Person:
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return self.name


class Persistence(ABC):
    @abstractmethod
    def save(self):
        pass

class DBStorage(Persistence):
    def save(self):
        print("Saving in DB.....")

class JSONStorage(Persistence):
    def save(self):
        print("Saving in JSON")


if __name__ == "__main__":
    person = Person("Anshu")
    db_storage = DBStorage()
    db_storage.save()
