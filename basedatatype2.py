# -*- coding: utf-8 -*-
# @Time    : 2020/10/21 14:12
# @Author  : Alex
"""
基本数据类型之list
"""

# enumerate函数

a = ['a', 'b', 'c']
for index, value in enumerate(a):
    print("第 {} 个字母为 {}".format(index, value))

# list 是可变数据类型
a[0] = 'd'
print(a[0])
