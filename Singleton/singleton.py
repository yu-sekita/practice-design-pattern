

class Singleton:

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls)
        return cls._instance

    @classmethod
    def get_instance(cls):
        return cls.__new__(cls)


class MySingleton(Singleton):

    def __init__(self):
        print('MySingleton', self)


# class MySingleton:

#     def __new__(cls, *args, **kwargs):
#         if not hasattr(cls, '_instance'):
#             cls._instance = super().__new__(cls)
#         return cls._instance

#     def __init__(self):
#         print('MySingleton', self)

#     @classmethod
#     def get_instance(cls):
#         return cls._instance
