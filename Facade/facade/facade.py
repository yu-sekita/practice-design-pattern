from abc import abstractmethod

from .html_writer import HtmlWriter
from .utils import write_text_file


class Facade:

    @abstractmethod
    def output(self, my_name):
        pass


class FacadePrintConsole(Facade):
    
    def output(self, my_name):
        html_writer = HtmlWriter()
        html_writer.body = f'<h1>Welcome to {my_name} page</h1>'
        print(html_writer.html)


class FacadeMakeHtml(Facade):
    
    def output(self, my_name):
        html_writer = HtmlWriter()
        html_writer.body = f'<h1>Welcome to {my_name} page</h1>'
        write_text_file(html_writer.html, 'index.html')
