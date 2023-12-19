"""
@Time: 2023/12/6 16:11
@Author: WQ
@File: test.py
@Des:
"""

slots = ['a{}'.format(i) for i in range(10000)]

class TestA(object):
    __slots__ = slots

    def __init__(self):
        for i in slots:
            self.__setattr__(i, i[1:])

class TestB(object):
    def __init__(self):
        for i in slots:
            self.__setattr__(i, i[1:])

if __name__ == '__main__':
    a = TestA()
    b = TestB()
    print(a.a0, a.a1, a.a2, a.a3, a.a4, a.a5, a.a6, a.a7, a.a8, a.a9)
    print(b)

