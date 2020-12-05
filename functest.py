# -*- coding: utf-8 -*-
# @Time    : 2020/10/21 14:12
# @Author  : Alex
"""
python 方法（函数）

return 语句会从函数内部返回一个值。
不带表达式参数的 return 会返回 None。
函数执行完毕退出也会返回 None。
"""


def fibo(num):
    """while循环实现斐波那契数列"""
    fib_list = []
    a, b = 0, 1
    while num > a:
        fib_list.append(a)
        a, b = b, a + b
    #  不做返回也会默认返回None
    # return 返回None
    return fib_list


# 默认参数值
# todo 默认值可以理解为现在函数外赋值，再传入函数，即 该值的作用域在函数外部， 当为可变数据类型时 会将数据改变
def sample_1(a_int, L=[]):  # 默认值只会执行一次。这条规则在默认值为可变对象（列表、字典以及大多数类实例）时很重要。
    """参数默认值"""
    L.append(a_int)
    return L


def today_say(*args, **kwargs):
    """
    *args: 包含除了已有形参列表以外的位置参数 -> 元组
    **kwargs: 包含除了与已有形参相对应的关键字参数以外的所有关键字参数 -> 字典
    *name 必须出现在 **name 之前
    """
    print(args)
    print("*args为{}类型".format(type(args)))
    print(kwargs)
    print("*args为{}类型".format(type(kwargs)))


def f1():
    """
    lambda表达式
    """


if __name__ == '__main__':
    # result = fibo(100)
    # print(result)
    print(sample_1(1))
    print(sample_1(1))
    # print(L=[5], 1) 关键字参数需要在位置参数后面
    print(sample_1(1, L=[8]))
    today_say("这是第一个位置参数", "这是第二个位置参数", kwargs_1="这是第一个关键字参数", kwargs_2="这是第二个关键字参数")
    # 解包参数 * 可以将list或tuple解为位置参数，**可以将字典解为关键词参数
    for i in range(*[1, 3]):
        print(i)
