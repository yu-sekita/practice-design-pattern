
from singleton import MySingleton


if __name__ == '__main__':
    s1 = MySingleton()
    s2 = MySingleton()
    s3 = MySingleton.get_instance()
    print('s1 == s2 ? ', s1 == s2)
    print('s2 == s3 ? ', s2 == s3)
    print('s1 == s3 ? ', s1 == s3)
