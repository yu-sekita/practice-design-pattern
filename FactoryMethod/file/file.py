
from abc import abstractmethod
import csv


class File:

    @abstractmethod
    def write(self, text, file_path):
        pass


class HTML(File):

    def __str__(self):
        return 'HTML Class'

    def write(self, users, file_path):
        body = self.__create_body(users)

        html = f"""
        <html>
        <head><title>Factory Method pattern</title></head>
        <body>{body}</body>
        </html>
        """
        with open(file_path, 'wt') as f:
            f.write(html)

    def __create_body(self, users):
        body = """
        <table>
            <tr>
                <th>ID</th>
                <th>name</th>
            </tr>
        """
        for user_id, name in users:
            tr = f"""
            <tr>
                <td>{user_id}</td>
                <td>{name}</td>
            </tr>
            """
            body += tr
        body += """
        </table>
        """
        return body


class CSV(File):

    def __str__(self):
        return 'CSV Class'

    def write(self, users, file_path):
        text = [['ID', 'name']]
        for user_id, name in users:
            user = [user_id, name]
            text.append(user)

        with open(file_path, 'wt') as f:
            csv_out = csv.writer(f)
            csv_out.writerows(text)
