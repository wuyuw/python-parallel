# -*- coding: utf-8 -*-
"""
    @Time    : 2021/3/4 3:57 下午
    @Author  : leiya
    @Email   : leiya@douyu.tv
    @FileName: demo02_name.py
"""

import multiprocessing
import time


def foo():
    name = multiprocessing.current_process().name
    print("Starting %s \n" % name)
    time.sleep(3)
    print("Exiting %s \n" % name)


if __name__ == '__main__':
    process_with_name = multiprocessing.Process(name='foo_process', target=foo)
    process_with_default_name = multiprocessing.Process(target=foo)
    process_with_name.start()
    process_with_default_name.start()