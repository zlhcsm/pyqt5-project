# -*- coding: utf-8 -*-

# @Time  : 2020-04-15 22:44

# @Author : 张磊

# @Desc : ==============================================

# Life is Short I Use Python!!!                      ===

# If this runs wrong,don't ask me,I don't know why;  ===

# If this runs right,thank god,and I don't know why. ===

# Maybe the answer,my friend,is blowing in the wind. ===

# ======================================================

# @Project : pyqt5-project

# @FileName: action.py

# @Software: PyCharm

# @  Blog:https://blog.csdn.net/zzzzlei123123123
import numpy as np


def get_message():
    """
    返回从串口中读取的数据
    :return:
    """
    num = np.random.randint(low=0, high=6)
    return str(num)