# class SomeClass(object):
#     attr1=42
#
#     def foo(self,x):
#         print(2*x)
# obj=SomeClass()
# obj.foo(6)
# print(obj.attr1)

# class Person:
#     def say(self,message):
#         print(message)
#
#     def say_hello(self):
#         self.say('Hello')
#
# tom=Person()
# tom.say_hello()

# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#     def display_info(self):
#         print(f'Name:{self.name}, Age:{self.age}')
# tom=Person(name='Tom', age=37)
# tom.display_info()


# class SomeClass(object):
#     def __init__(self,name):
#         self.name=name
#         print(f'проинициализировал объект {self.name} класса SomeClass')
#     def __del__(self):
#         print(f'удаляет объект {self.name} класса SomeClass')
# obj=SomeClass('Bob')
# del obj


# class Example:
#     a=2
#     b=3
#     def __init__(self,t,r):
#         self.t=t
#         self.r=r
#     def func(self):
#         self.c=5
#         print(self.c)
#     def func1(self):
#         return self.a+self.b
#     def func2(self):
#         return self.t**self.r
#
# example=Example(4,2)
# print(example.a)
# print(example.func1())
# print(example.func2())

# class Car:
#     def __init__(self, color, car_type, year):
#         self.color = color
#         self.type = car_type
#         self.year = year
#
#     def func3(self):
#         print('Автомобиль заведен')
#
#     def func4(self):
#         print('Автомобиль заглушен')
#
#     def func(self):
#         print(self.color)
#
#     def func1(self):
#         print(self.type)
#
#     def func2(self):
#         print(self.year)
#
#
# car = Car("Черный", "Рено Логан", 1900)
# car.func3()
# car.func1()
# car.func2()
# car.func()
# car.func4()


# class Computer:
#     def __init__(self):
#         self.__price=900
#     def get_price(self):
#         print(f' Цена продажи {self.__price}')
#     def self_price(self,price):
#         self.__price=price
# c=Computer()
# c.get_price()
# c.self_price(1000)
# c.get_price()


# class Figure:
#     def __init__(self,height=2,width=2):
#         self.height=height
#         self.width=width
#     def get_height(self):
#         return self.height
#     def set_height(self,height):
#         if height>0:
#             self.height=height
#         else:
#             raise Exception()
#     def set_width(self,width):
#         if width>0:
#             self.width=width
#             raise Exception()
# figure=Figure()
# print(figure.get_height())
# print(figure.set_width())



# class Mine:
#     def __init__(self):
#         self._x=None
#     def get_x(self):
#         return self._x
#     def set_x(self,value):
#         self._x=value
#     def del_x(self):
#         self._x='No more'
#     x=property(get_x,set_x,del_x,'property x')
# print(type(Mine.x))
# mine=Mine()
# print(mine.x)


# class Mine:
#     def __init__(self):
#         self.x = 'some none'
#
#     @property
#     def prop(self):
#         return self.x
#
#     @prop.setter
#     def prop(self, value):
#         self.x = value
#
#     @prop.deleter
#     def prop(self):
#         del self.x
#
#
# mine = Mine()
# print(mine.prop)
# mine.prop = 'some new value'
# del mine.prop


# class Person:
#     def __init__(self, name):
#         self._name = name
#
#     @property
#     def name(self):
#         print('Getting name')
#         return self._name
#
#     @name.setter
#     def name(self, value):
#         print('Setting name to ' + value)
#         self._name = value
#
#     @name.deleter
#     def name(self):
#         print('Deleting name')
#         del self._name
#
# p = Person('Bob')
# print('The name is:', p.name)
# p.name = 'John'
# del p.name

#
# class Parent1:
#     def method1(self):
#         print('Метод от Parent1')
# class Parent2:
#     def method2(self):
#         print('Метод от Parent2')
# class Child(Parent1, Parent2):
#     def child_method(self):
#         print('Метод от Child')
#
#
# child = Child()
# child.method1()
# child.method2()


# class D:
#     attr=3
# class B(D):
#     pass
# class E:
#     attr=2
# class C(E):
#     attr=1
# class A(B,C):
#     pass
# X=A()
# print(X.attr)
# MRO=[X,A,B,D,C,E,object]


# class Soda():
#     def __init__(self,flavor=None):
#         self.flavor=flavor
#     def __str__(self):
#         if self.flavor:
#             return f'у вас есть газировка с{self.flavor} вкусом'
#         else:
#             return f'у вас обычная газировка'
# soda1=Soda('клубничная')
# print(soda1)
# soda2=Soda()
# print(soda2)


# class Math:
#     def __init__(self):
#         pass
#     def add(self, a, b):
#         return a + b
#     def sub(self, a, b):
#         return a - b
#     def mul(self, a, b):
#         return a * b
#     def div(self, a, b):
#         return a / b
# a = int(input())
# b = int(input())
# math = Math()
# print(math.div(a, b))
# print(math.mul(a, b))
# print(math.add(a, b))
# print(math.sub(a, b))


# class Sphere:
#     def __init__(self,radius=1,x=0,y=0,z=0):
#         self.radius=radius
#         self.x=x
#         self.y=y
#         self.z=z
#     def get_volume(self):
#         return 4/3*3.14*self.radius**3
#     def get_square(self):
#         return 4*3.14*self.radius**2
#     def get_radius(self):
#         return self.radius
#     def get_center(self):
#         return (self.y,self.x,self.z)
#     def set_center(self,x,y,z):
#         self.x=x
#         self.y=y
#         self.z=z
#     def set_radius(self,radius):
#         self.radius=radius
#         return self.radius
# sphere=Sphere()
# print(sphere.get_center())
# print(sphere.get_radius())
# print(sphere.get_volume())
# print(sphere.get_square())

a = int(input())
if a % 2 != 0:
    print('YES')
elif 2 <= a <= 5:
    print('NO')
elif 6 <= a <= 20:
    print('YES')
else:
    print('NO')













