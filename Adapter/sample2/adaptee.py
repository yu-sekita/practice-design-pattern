

class Adaptee:

    def __init__(self, message):
        self._message = message

    def show_message(self):
        print(self._message)

    def show_message_with_line(self):
        print('---- {} ----'.format(self._message))
