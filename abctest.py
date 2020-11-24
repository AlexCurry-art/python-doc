# -*- coding: utf-8 -*-
# @Time    : 2020/10/21 14:12
# @Author  : Alex
"""
https://blog.louie.lu/2017/07/28/%E4%BD%A0%E6%89%80%E4%B8%8D%E7%9F%A5%E9%81%93%E7%9A%84-python-%E6%A8%99%E6%BA%96%E5%87%BD%E5%BC%8F%E5%BA%AB%E7%94%A8%E6%B3%95-03-abc/
https://blog.csdn.net/weixin_40907382/article/details/80277170
"""
import abc


# 将Animal 作为抽象类
class Animal(abc.ABC):
    # 等同于 class Animal(metaclass=abc.ABCMeta):
    """
    抽象类是一个特殊的类，只能被继承，不能实例化
    因为有未被实现的抽象方法
    """

    @abc.abstractmethod
    def screaming(self):
        return NotImplemented

    @abc.abstractmethod
    def walk(self, x, y):
        return NotImplemented


class Person:
    """"
    将人注册为动物
    """

    @staticmethod
    def thinking():
        print("正在思考")


class Dog(Animal):
    """
    抽象类的抽象方法必须被实现
    否则会报错
    """

    def screaming(self):
        print("wolf")

    def walk(self, x: int, y: int) -> tuple:
        return x, y


class Base(abc.ABC):
    """类方法也可以抽象化"""

    @classmethod
    @abc.abstractmethod
    def setUpClass(cls):
        return NotImplemented

    @staticmethod
    @abc.abstractmethod
    def count(self, data):
        return len(data)


class Implementation(Base):

    @classmethod
    def setUpClass(cls):
        cls.count = 0

    @staticmethod
    def count(self, data):
        self.count = len(data)
        return self.count


if __name__ == '__main__':
    # animal = Animal()
    dog = Dog()
    dog.screaming()
    walk = dog.walk(10, 20)
    print(walk)

    #     isinstance()
    print(type(dog))
    if isinstance(dog, Animal):
        print("Dog 是 Animal 类型")
    if issubclass(Dog, Animal):
        print("Dog 是 Animal 子类")

    # register
    Animal.register(Person)  # 将人注册为动物
    # 将其他的类”注册“到抽象基类下当虚拟子类（调用register方法），虚拟子类的好处是你实现的第三方子类不需要直接继承自基类，可以实现抽象基类中的部分API接口，也可以根本不实现，但是issubclass(),
    # issubinstance()进行判断时仍然返回真值。
    person = Person()
    if isinstance(person, Animal):
        print("人也是一种你动物")
