from adaptee import Adaptee
from target import Target


class Adapter(Adaptee, Target):

    def __init__(self, message):
        super().__init__(message)
    
    def print_message(self):
        self.show_message()

    def print_message_with_line(self):
        self.show_message_with_line()
