from persistance import Persistance
class Jounel:
    def __init__(self) -> None:
        self.entries = []
        self.count = 0
    
    def add_entries(self,entry):
        self.entries.append(f"{self.count}:{entry}")
        self.count+=1
    
    def removee_entries(self,position):
        del self.entries[position]

    def __repr__(self) -> str:
        return "\n".join(self.entries)
    #Till Here this class is doing one thing at one time

    def save(self):
        pass

    def load(self):
        pass

    # Above two methods are very separate from working of this class
    # So Defined one more class Persistence


if __name__ == "__main__":
    j = Jounel()
    j.add_entries("I am anshu Mishra")
    j.add_entries("I am anshu Mishra")
    Persistance.save()
    print(j)