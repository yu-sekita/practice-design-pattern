

class Context:

    def __init__(self, strategy):
        self._strategy = strategy

    def print_text(self, text):
        print(self._strategy.next_line(text))
