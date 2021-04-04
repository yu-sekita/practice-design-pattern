
from creator import CSVCreator, HTMLCreator


if __name__ == '__main__':
    file_type = input('please input file type: ')

    if file_type == 'csv':
        file_path = 'test.csv'
        creator = CSVCreator()
    else:
        file_path = 'test.html'
        creator = HTMLCreator()

    users = [
        ('001', 'Taro'),
        ('002', 'Jiro')
    ]
    file = creator.create()
    file.write(users, file_path)
