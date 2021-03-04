# -*- coding: utf-8 -*-
"""
    @Time    : 2021/3/4 1:41 下午
    @Author  : leiya
    @Email   : leiya@douyu.tv
    @FileName: demo01.py
"""

import threading
import time


def function(i):
    print("function called by thread %i\n" % i)
    time.sleep(1)
    print("thread %i exiting" % i)


if __name__ == '__main__':
    threads = []
    for i in range(5):
        t = threading.Thread(target=function, args=(i, ))
        threads.append(t)
        t.start()