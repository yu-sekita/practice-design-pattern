
from abc import abstractmethod

from file import HTML, CSV


class FileCreator:

    @classmethod
    def create(cls):
        file = cls.create_file()
        print(f'created {file}')
        return file

    @classmethod
    @abstractmethod
    def create_file(cls):
        pass


class HTMLCreator(FileCreator):

    @classmethod
    def create_file(cls):
        return HTML()


class CSVCreator(FileCreator):

    @classmethod
    def create_file(cls):
        return CSV()
