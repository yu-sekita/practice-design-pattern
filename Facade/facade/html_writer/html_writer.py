

class HtmlWriter:

    def __init__(self):
        self._html = '''
        <html>
        <head>{}</head>
        <body>{}</body>
        </html>
        '''

        self._head = '<title>home</title>'
        self._body = ''

    @property
    def html(self):
        return self._html.format(self._head, self._body)

    @property
    def body(self):
        return self._body

    @body.setter
    def body(self, body):
        self._body = body
