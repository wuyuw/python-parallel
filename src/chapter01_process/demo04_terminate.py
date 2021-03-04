# -*- coding: utf-8 -*-
"""
    @Time    : 2021/3/4 4:13 下午
    @Author  : leiya
    @Email   : leiya@douyu.tv
    @FileName: demo04_terminate.py
"""

import multiprocessing
import time


def foo():
        print('Starting function')
        time.sleep(1)
        print('Finished function')


if __name__ == '__main__':
        p = multiprocessing.Process(target=foo)
        print('Process before execution:', p, p.is_alive())
        p.start()
        print('Process running:', p, p.is_alive())
        time.sleep(0.5)
        p.terminate()
        print('Process terminated:', p, p.is_alive())
        p.join()
        print('Process joined:', p, p.is_alive())
        print('Process exit code:', p.exitcode)