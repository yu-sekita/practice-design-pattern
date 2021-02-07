from facade import FacadeMakeHtml, FacadePrintConsole


if __name__ == '__main__':
    facade = FacadePrintConsole()
    facade.output(my_name='tanaka taro')

    facade = FacadeMakeHtml()
    facade.output(my_name='tanaka jiro')
