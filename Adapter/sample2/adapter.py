from adaptee import Adaptee
from target import Target


class Adapter(Target):

    def __init__(self, message):
        self._adaptee = Adaptee(message)
    
    def print_message(self):
        self._adaptee.show_message()

    def print_message_with_line(self):
        self._adaptee.show_message_with_line()
