from adapter import Adapter


if __name__ == '__main__':
    target = Adapter('target message')

    target.print_message()
    target.print_message_with_line()
