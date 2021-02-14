from context import Context
from strategy import StrategyA, StrategyB


if __name__ == '__main__':
    simple_context = Context(StrategyA())
    advance_context = Context(StrategyB())

    text = '''
    こちらはテスト用テキストになります。
    simpleバージョンはは改行コード毎に空行を加え、
    advanceバージョンは偶数の改行コード毎に空行を加えます。
    以上。
    '''
    print('----- simple version -----')
    simple_context.print_text(text)
    print('----- advance version -----')
    advance_context.print_text(text)
