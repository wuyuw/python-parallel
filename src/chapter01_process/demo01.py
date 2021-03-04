# -*- coding: utf-8 -*-
"""
    @Time    : 2021/3/4 3:45 下午
    @Author  : leiya
    @Email   : leiya@douyu.tv
    @FileName: demo01.py
"""

import multiprocessing


def foo(i):
    print('called function in process: %s' % i)
    return


if __name__ == '__main__':
    Process_jobs = []
    for i in range(5):
        p = multiprocessing.Process(target=foo, args=(i,))
        Process_jobs.append(p)
        p.start()
        p.join()
