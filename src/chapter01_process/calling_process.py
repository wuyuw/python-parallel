# -*- coding: utf-8 -*-
"""
    @Time    : 2021/3/4 11:28 上午
    @Author  : leiya
    @Email   : leiya@douyu.tv
    @FileName: calling_process.py
"""

import os

# this is the code to execute
program = "python"
print("Process calling")
arguments = ["called_Process.py"]

# we call the called_Process.py script
os.execvp(program, (program,) + tuple(arguments))
print("Good Bye!!")