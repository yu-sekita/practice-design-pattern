
from abc import abstractmethod

from file import HTML, CSV


class FileCreator:

    @abstractmethod
    def create_file(self):
        pass


class HTMLCreator(FileCreator):

    def create_file(self):
        return HTML()


class CSVCreator(FileCreator):

    def create_file(self):
        return CSV()
