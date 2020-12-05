# -*- coding: utf-8 -*-
# @Time    : 2020/10/21 14:12
# @Author  : Alex
"""
python 流程控制
"""


# 循环结构 1循环变量初始化 2循环条件 3循环变量的改变
# for 遍历循环
# todo 在遍历同一个集合时修改该集合的代码可能很难获得正确的结果。通常，更直接的做法是循环遍历该集合的副本或创建新集合
def odd_or_even(num):
    """判断指定范围内的奇偶数"""
    for i in range(num):
        if i % 2 == 0:
            print("{} 是偶数".format(i))
        else:
            print("{} 是奇数".format(i))
    else:
        print("结束")


def find_prime(num):
    """指定范围内的素数"""
    for i in range(2, num):  # 最小的素数是2
        for j in range(2, i):  # 素数: 不能被1和它本身之外的数字整除的数
            if i % j == 0:
                break
        else:  # 在for循环结构中, else 子句则会在未发生 break 时执行
            print("{} 是素数".format(i))


# while 无限循环
def fibo_1(num):
    """while循环实现斐波那契数列"""
    a, b = 0, 1
    while num > a:
        print(a)
        a, b = b, a + b  # 多重赋值 右手边的表达式，在任何赋值发生之前就被求值了。右手边的表达式是从左到右被求值的。


if __name__ == '__main__':
    # fibo_1(100)
    # prime_or_equals(100)
    find_prime(100)
