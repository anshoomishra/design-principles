# A single class must have its core responsiblity only

class Person:
    def __init__(self,name):
        self.name = name
    
    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

    def save_into_db(self):
        print(f"Saving into DB {self}")

if __name__ == "__main__":
    p = Person("Anshu")
    p.save_into_db()
        