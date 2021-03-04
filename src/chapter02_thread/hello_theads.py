# -*- coding: utf-8 -*-
"""
    @Time    : 2021/3/4 11:35 上午
    @Author  : leiya
    @Email   : leiya@douyu.tv
    @FileName: hello_theads.py
"""

from threading import Thread
import time

# To create a thread in Python you'll want to make your class work as a thread.
# For this, you should subclass your class from the Thread class


class HelloThead(Thread):

    def print_message(self, x):
        print(f"{x}in print_message")

    def run(self):
        print("Thread Starting\n")
        x = 0
        while x < 10:
            self.print_message(x)
            time.sleep(2)
            x += 1
        print("Thread Ended\n")


def run_daemon():
    """子线程设为守护线程，则主线程结束时子线程结束"""
    ht = HelloThead(daemon=True)
    ht.start()
    # 主线程等待子线程执行完后再往下执行
    ht.join()


def run():
    """子线程为非守护线程，则主线程结束后子线程继续执行"""
    ht = HelloThead()
    ht.start()


if __name__ == '__main__':
    print("Process Started")
    # run_daemon()
    run()
    print("Process Ended")
