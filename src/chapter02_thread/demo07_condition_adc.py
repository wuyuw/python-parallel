# -*- coding: utf-8 -*-
"""
    @Time    : 2021/3/4 3:06 下午
    @Author  : leiya
    @Email   : leiya@douyu.tv
    @FileName: demo07_condition_adc.py
"""

from threading import Thread, Condition

"""
开3个线程，顺序打印ABC
"""

condition = Condition()
current = "A"


class ThreadA(Thread):
    def run(self):
        global current
        for _ in range(10):
            with condition:
                while current != "A":
                    condition.wait()
                print("A")
                current = "B"
                condition.notify_all()


class ThreadB(Thread):
    def run(self):
        global current
        for _ in range(10):
            with condition:
                while current != "B":
                    condition.wait()
                print("B")
                current = "C"
                condition.notify_all()


class ThreadC(Thread):
    def run(self):
        global current
        for _ in range(10):
            with condition:
                while current != "C":
                    condition.wait()
                print("C")
                current = "A"
                condition.notify_all()


if __name__ == '__main__':
    a = ThreadA()
    b = ThreadB()
    c = ThreadC()

    a.start()
    b.start()
    c.start()

    a.join()
    b.join()