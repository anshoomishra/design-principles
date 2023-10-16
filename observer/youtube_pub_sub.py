from abc import ABC, abstractmethod
import logging

logger = logging.getLogger("design patters")


class YouTubeSubscriber(ABC):
    @abstractmethod
    def send_notification(self, event):
        pass


class YouTubeUser(YouTubeSubscriber):
    def __init__(self,name):
        self.name = name

    def send_notification(self,name, event):
        logger.info(f"User {self.name} subscriber of channel {name} got {event}")
        print(f"User {self.name} subscriber of channel {name} got {event}")


class YouTube:
    def __init__(self, name):
        self.name = name
        self.subs = []

    def subscribe(self,sub):
        self.subs.append(sub)

    def notify(self,event):
        for sub in self.subs:
            sub.send_notification(self.name,event)


if __name__ == "__main__":
    channel = YouTube("Anshu Tutor")
    channel.subscribe(YouTubeUser("Ankit"))
    channel.subscribe(YouTubeUser("Anjali"))
    channel.subscribe(YouTubeUser("Sachin"))
    channel.notify("Video Uploaded - How to speak english ")

