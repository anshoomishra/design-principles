from abc import ABC,abstractmethod

class Notification(ABC):
    @abstractmethod
    def notify(self,message):
        pass

class Email(Notification):
    def __init__(self,email):
        self.email = email
    
    def notify(self,message):
        print(f"Sending {message} to {self.email}")


class SMS(Notification):
    def __init__(self,phone):
        self.phone = phone
    
    def notify(self,message):
        print(f"Sending {message} to {self.phone}")

class NotificationManager():
    def __init__(self,notification):
        self.notification = notification

    def notify(self,message):
        self.notification.notify(message)

class Contact:
    def __init__(self):
        self.name = None 
        self.mob = None
        self.email = None
        self.address = None

    def set_name(self,name):
        self.name = name

    def set_mob(self,mob):
        self.mob = mob
    
    def set_email(self,email):
        self.email = email
    
    def set_address(self,address):
        self.address = address

class ContactBuilder:
    def __init__(self):
        self.contact = Contact()
    
    def add_name(self,name):
        self.contact.set_name(name)
        return self
    def add_mob(self,mob):
        self.contact.set_mob(mob)
        return self
    def add_email(self,name):
        self.contact.set_email(name)
        return self
    def add_address(self,address):
        self.contact.set_address(address)
        return self
    def build(self):
        return self.contact
        
if __name__ == "__main__":
    contact = ContactBuilder() \
        .add_name("Anshu") \
            .add_mob(7007975402) \
                .add_email("anshum45@gmail.com") \
                    .build()

    email_notification = Email(contact.email)
    nm = NotificationManager(email_notification)
    nm.notify(message="Hi how are you")



