# class Pizza:
#     def __init__(self,ingridient):
#         self.__ingridient=ingridient
#
#     def __str__(self):
#         return f'Pizza({self.ingridient})'
#
#     @classmethod
#     def margharita(cls):
#         return cls(['tomatos'])
#
#     def margharita2(cls):
#         return cls(['cheaz'])
#
# print('Pizza.margharita()')
# print('Pizza.margharita2()')

# class Calculator:
#     @staticmethod
#     def add(a,b):
#         return a+b
#
#     @staticmethod
#     def sub(a,b):
#         return a-b
#
#     @staticmethod
#     def mul(a,b):
#         return a*b
#
#     @staticmethod
#     def div(a,b):
#         return a/b
#
# print('введите входные данные')
# x=int(input())
# y=int(input())
# print(Calculator.add(x,y))
# print(Calculator.sub(x,y))
# print(Calculator.mul(x,y))
# print(Calculator.div(x,y))

# from dataclasses import dataclass
# @dataclass(order=True)
# class Foo:
#     num1: float
#     num2: float
# bill1 = Foo(num1=50.5, num2=7.5)
# bill2 = Foo(num1=50.5, num2=8.0)
# print(bill1<bill2)

# class Rectangle:
#     def __init__(self,widht,height):
#         self.widht=widht
#         self.height=height
#
#     def area(self):
#         return self.widht*self.height
#     def per(self):
#         return (self.widht+self.height)*2
#     def dig(self):
#         return (((self.widht**2))+((self.height**2))**0.5)
#
# rectangle = Rectangle(4,3)
# print(rectangle.area())
# print(rectangle.per())
# print(rectangle.dig())

# class BankAccount:
#     def __init__(self,balance=0):
#         self.balance=balance
#     def dep(self,a):
#         self.balance+=a
#         return f'{a} зачислено.Баланс {self.balance}'
#     def withdraw(self,a):
#         self.balance-=a
#         return f'{a} снято. Баланс{self.balance}'
#     def check_balance(self):
#         return f'Баланс{self.balance}'
# bank=BankAccount(100)
# print(bank.check_balance())
# print(bank.dep(100))
# print(bank.withdraw(100))

# class Library:
#     def __init__(self):
#         self.books=[]
#     def add_book(self,book):
#         self.books.append('book')
#         return self.books
#     def remove_book(self,book):
#         if book in self.books:
#             self.books.remove('book')
#         return self.books
#     def find_book(self,title):
#         if title in self.books:
#             return True
#         return False
# library=Library()
# print(library.add_book('book1'))
# print(library.remove_book('book2'))
# print(library.find_book('book2'))


# class Item:
#     def __init__(self, arg):
#         self.arg = arg
#
#     def __str__(self):
#         return str(self.arg)

# class Container:
#     def __init__(self, *args):
#         self.items_list = list()
#         for i in args:
#             self.items_list.append(Item(i))
#
#     def __getitem__(self, i):
#         return self.items_list[i]
#
# g = Container(5, 10, 'abc')
# print(g.items_list[1])
# print(g[0])
# print(g[2])


# class Point:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f'({self.x},{self.y})'
#
#     def __add__(self, other):
#         x = self.x + other.x
#         y = self.y + other.y
#         return Point(x, y)
#
#
# p1 = Point(1, 2)
# p2 = Point(1, 3)
# p3 = p1 + p2
# print(p3)


# class Student:
#     def __init__(self, name):
#         self.name = name
#         self.grades = []
#
#     def add_grades(self, grade):
#         self.grades.append(grade)
#
#     def average_grade(self):
#         if self.grades:
#             return sum(self.grades) / len(self.grades)
#         else:
#             return 0
#
#     def student_info(self):
#         return f'Имя: {self.name}, Средний балл: {self.average_grade()}'
#
# student = Student('Bob')
# student.add_grades(5)
# student.add_grades(4)
# student.add_grades(3)
# print(student.student_info())


# class Franction:
#     def __init__(self,num,den):
#         self.num=num
#         self.den-den
#     def __add__(self,other):
#         new_num=self.num*other.den+other.num*self.den
#         nwe_den=self.dem*other.den
#         return Franction(new_num,nwe_den)



# Someclass=type('Myclass',(),{})
# print(Someclass)
# print(Someclass())

# class Upper(type):
#     def __new__(cls,clsname,bases,dct):
#         uppercase_attr={}
#         for name,val in dct.items():
#             if not name.startswitch('__'):
#                 uppercase_attr[name.upper()]=val
#             else:
#                 uppercase_attr[name]=val
#         return super(Upper,cls).__new__(cls,clsname,bases,uppercase_attr)


# class book(model):
#     title=models.CharField(max_lenght=1000)
#
#     def __str__(self):
#         return self.title
#
#
# class SeriaLazierBook:
#     class Meta:
#         model=book
#         fields=['title']


# class Mixin:
#     def add_method(self):
#         return 'Это доп метод'
#
# class MixinMeta(type):
#     def __new__(cls, name, bases, dct):
#         dct.update(Mixin().__dict__)
#         return super().__new__(cls, name, bases, dct)
#
# class BaseClass(metaclass=MixinMeta):
#     def base_method(self):
#         return 'Это базовый метод'
#
# obj = BaseClass()
# print(obj.base_method())
# print(obj.add_method())

# class Singleton(type):
#     _instances = {}
#     def __call__(cls, *args, **kwargs):
#         if cls not in cls._instances:
#             cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
#         return cls._instances[cls]
#
# class MyClass(metaclass=Singleton):
#     def __init__(self, value):
#         self.value = value
#
# obj1 = MyClass(10)
# obj2 = MyClass(20)
# print(obj2.value)
# print(obj1.value)







        





















        


        



        


        










