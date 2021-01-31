from abc import abstractmethod


class Target:
    @abstractmethod
    def print_message(self):
        raise NotImpremetedError()

    @abstractmethod
    def print_message_with_line(self):
        raise NotImpremetedError()
