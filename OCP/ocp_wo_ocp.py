# Open closed prinple syas that - A class must be opne for extension for closed
# for modification 

## This program has problem - what if we want to one more type of saving 

class Person:
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return self.name


class PersonDB:
    def save_in_db(self):
        print("Saving in DB......")

    def save_in_json(self):
        print("Saving in JSON")

if __name__ == "__main__":
    person = Person("Anshu")
    pd = PersonDB()
    pd.save_in_db()

