# -*- coding: utf-8 -*-
# @Time    : 2020/11/27 14:19
# @Author  : xieyafei
"""
命名规则与规范
https://www.cnblogs.com/liuyanhang/p/11344149.html

规则：
变量名可以包括字母、数字、下划线
数字不能做为开头
系统关键字不能做变量名使用

规范：
模块 尽量使用小写命名，尽量不要用下划线
类: 大驼峰 所有单词首字母大写
常量 所有字母大写 单词之间下划线
"""


class FirstClass(object):
    # 变量及函数名 小写 单词之间下划线
    def __init__(self):
        self.first_var = "first"

    def print_first_var(self):
        print(self.first_var)


SUCCESS_CODE = 200
