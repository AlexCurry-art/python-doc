# -*- coding: utf-8 -*-
# @Time    : 2020/10/21 14:12
# @Author  : Alex
"""
sys 主要用于和python解释器交互
常用函数：
sys.argv: 命令行参数列表 第一个元素为脚本名称
"""

import sys
import time


def get_argv():
    """
    sys.argv: 命令行参数列表 第一个元素为脚本名称
    """
    print("获取命令行参数")
    for arg_index, arg_value in enumerate(sys.argv):
        print("第{}个参数为：{}".format(arg_index, arg_value))


def get_path():
    """
    sys.path 返回模块搜索路径
    sys.path.append(path) 添加模块搜索路径
    """
    sys.path.append(r"C:\Users\Alex\Desktop")
    print(sys.path)


def get_modules():
    """
    sys.modules: 记录已导入的模块, 当第二次再导入该模块时，python会直接到字典中查找，从而加快了程序运行的速度。它拥有字典所拥有的一切方法。
    :return: 全局字典
    """
    print(sys.modules)
    import xlwt
    print(sys.modules)


def test_exit(exit_value):
    """
    sys.exit(n) n=0正常退出 其他为异常退出
    可以被捕获
    :return:
    """
    try:
        sys.exit(exit_value)
    except SystemExit as e:
        print("捕获异常退出：{}".format(e))
        # 未捕获此异常 程序直接退出
        sys.exit(0)


def other_def():
    """
    sys 的其他方法
    :return:
    """
    print(sys.version)
    print(sys.platform)  # 会常用
    for i in range(50):
        sys.stdout.write("*")  # 打印*号，类似于print，但是默认不换行
        time.sleep(0.1)
        # sys.stdout.flush()  # #刷新，显示到屏幕上


if __name__ == '__main__':
    get_argv()
    get_path()
    # test_exit(8)
    get_modules()
    other_def()
