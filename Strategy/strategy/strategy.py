from abc import abstractmethod


class Strategy:

    @abstractmethod
    def next_line(self, text):
        pass


class StrategyA(Strategy):

    def next_line(self, text):
        return text.replace('\n', '\n\n')


class StrategyB(Strategy):

    def next_line(self, text):
        count = 0
        texts = ''
        for s in text:
            if s == '\n':
                count += 1
                if count % 2 == 0:
                    s = '\n\n'
            texts += s
        return texts
