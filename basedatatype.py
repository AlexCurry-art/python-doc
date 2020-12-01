# -*- coding: utf-8 -*-
# @Time    : 2020/11/27 17:07
# @Author  : xieyafei
"""
基本数据类型
Number（数字）
String（字符串）
List（列表）
Tuple（元组）
Set（集合）
Dictionary（字典）
"""

# Number
# 整型(Int) - 通常被称为是整型或整数，是正或负整数，不带小数点。
# 长整型(long integers) - 无限大小的整数，整数最后是一个大写或小写的L。
# 浮点型(floating point real values) - 浮点型由整数部分与小数部分组成，浮点型也可以使用科学计数法表示（2.5e2 = 2.5 x 102 = 250）
# 复数(complex numbers) - 复数由实数部分和虚数部分构成，可以用a + bj,或者complex(a,b)表示， 复数的实部a和虚部b都是浮点型。

# 运算符

a, b = 21, 6

#  + - * / //(除法取整数部分) % **(乘方)

print(a + b)  # 27
print(a - b)  # 15
print(a / b)  # 3.5 type为float
print(a // b)  # 3
print(a % b)  # 3
print(2 ** 3)  # 8
print(a + 2.1)  # 23.1 包含多种混合类型运算数的运算会把整数转换为浮点数

# 字符串 '...' 或 "。。。" 都可以
print('I\'m Alex')  # /(反斜杠用于转义)
print("I'm Alex")  # 用两种不同的引号避免
print('"Isn\'t," they said.')

print(r'I\'m Alex')  # r'' 的作用是去除转义字符.  常用于正则 对应re 模块
print(type(b'input'))  # b'' 代表bytes
print(u'unicode字符串')  # u''  代表是unicode编码的字符串，一般py文件已经定义编码格式为utf-8 无需再次指定
name = 'Alex'
print(f'{name} is 15 age')  # f''表示在字符串内支持大括号内的python 表达式, 及format的用法

# \   在行尾时是     续行符
# \\   反斜杠符号
# \' 单引号
# \"  双引号
# \a  响铃
# \b  退格
# \e  转义
# \000 　空　
# \n     换行
# \v　　纵向制表符
# \t      横向制表符
# \r    回车
# \f     换页
# \oyy   八进制数，yy代表字符，如 \o12 代表换行
# \xyy  十六进制数  yy代表字符，如\x0a代表换行
# \other 其他字符一普通格式输出

# 相邻字符串会合并 仅限于字面值（表俩个或者表达式不可以）
text = (
    'Put several strings within parentheses '
    'to have them'
    'joined together.')
print(text)

# ”“”。。。“”“字符串可以实现跨行输入
# 回车换行会自动包含到字符串中，
# 如果不想包含，在行尾添加一个 \ 即可
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")
# 字符串是可以被索引的
word = "python"
print(word[0])
print(word[-1])  # 注意 -0 和 0 是一样的，所以负数索引从 -1 开始
print(word[:3])  # 字符串支持切片
print(print(word[:3]+word[3:]))  # 切片 包含首 不包含尾 且切片有默认值

"""
 +---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+
 0   1   2   3   4   5   6
-6  -5  -4  -3  -2  -1
"""
# print(word[42]) indexError 越界错误
print(word[:42])  # 切片会自动处理

# word[0] = 'a' # str是不可变类型
# word[2:] = 'py' # str是不可变类型

# 可以新建
print("C"+word[1:])
print(len(word))

