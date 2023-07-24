class Person:
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return self.name
    
class PersonDB:
    def saving_into_DB(self,obj):
        print(f"Saving into DB {obj}")

if __name__ == "__main__":
    p = Person("Anshu")
    persondb = PersonDB()
    persondb.saving_into_DB(p)

