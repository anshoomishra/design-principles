class Notification:
    def notify(self,message,email):
        pass

class SMSNotification:
    def notify(self,message,mob):
        print(f"sending message - {message} - to {mob}")

class EmailNotification:
    def notify(self,message,email):
        print(f"sending message - {message} - to {mob}")


if __name__ == "__main__":
    smsNotification = SMSNotification()
    smsNotification.notify("Hi how are you","7007975402")
