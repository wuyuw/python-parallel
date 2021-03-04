# -*- coding: utf-8 -*-
"""
    @Time    : 2021/3/4 4:24 下午
    @Author  : leiya
    @Email   : leiya@douyu.tv
    @FileName: demo05_subclass.py
"""
import time
import multiprocessing


class MyProcess(multiprocessing.Process):
    def run(self):
        time.sleep(1)
        print('called run method in process: %s' % self.name)
        return


if __name__ == '__main__':
    jobs = []
    for i in range(5):
        p = MyProcess()
        jobs.append(p)
        p.start()
        # p.join()
    print("main process over")
