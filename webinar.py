# class DataBase:
#     def connect(self):
#         print('connect')
#
#     @staticmethod  # убираем self и добавляем @staticmethod и метод становится классической функцией
#     def select():
#         print('select')
#
#
# DataBase().select()  # создается экземпляр класса
#
# DataBase.select()  # работает в обоих случая

# class MyClass:
#     @classmethod
#     def my_method(cls, param):
#         print(cls(), param)  # сли поставить cls(), то можно обратиться к дургому методу класса, не создавая экземпляр класса
#
#
# print(MyClass)
# my = MyClass()
# my.my_method(10)
#
# MyClass.my_method(10)

# class Customer:
#     """Это класс покупатель"""
#     def __init__(self, name, phone):
#         self.name = name
#         self.phone = phone
#
#
# john = Customer('John', 654632654)
# john.x = 0
# print(john.__dict__)  # выводит словарь с key - переменной и val - ее значением
# print(john.__doc__)  # описание класса
# a = 0
# print(a.__doc__)  # будет описание int
# print(john.__class__.__name__)  # название класса объекта
# print(john.__module__)  # если класс импортировался из другого файла, то будет путь к нему


########## Создание ООП-программы ##########

# class Person:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     def __str__(self):
#         return f'{self.name} {self.surname}'
#
#
# class Teacher(Person):
#     def to_teach(self, subject, *students):
#         for student in students:
#             student.to_take(subject)
#
#
# class Student(Person):
#     def __init__(self, name, surname):
#         super().__init__(name, surname)
#         self.knowledge = []
#
#     def to_take(self, subject):
#         self.knowledge.append(subject)
#
#
# class Subject:
#     def __init__(self, *subjects):
#         self.subjects = subjects
#
#     def __str__(self):
#         return f'{self.subjects}'
#
#
# s = Subject('math', 'physics')
# print(s)
# t = Teacher('Ivan', "Ivanov")
# p_1 = Student('Petr', 'Petrov')
# p_2 = Student('Sidr', 'Sidorov')
# p_3 = Student('Jassie', 'Pinkman')
#
# t.to_teach(s, p_1, p_2)
# print(p_1.knowledge[0])
# print(p_2.knowledge[0])
# print(p_3.knowledge)

########## Создание собственных исключений ##########

# class OwnException(Exception):  # наследуемся от класса с исключениями
#     def __init__(self, txt):
#         self.txt = txt
#
#
# a = int(input('введите положительное число '))
# try:
#     if a < 0:
#         raise OwnException('отрицалово')  # выводит ошибку "отрицалово"
#     else:
#         print(a)
# except OwnException:
#     print('было введено отрицательное число')  # выводит сообщение при ошибке
#
# class my_dict(dict):  # можно унаследоваться от другого класса, например, словаря и модифицировать его
#     pass

# import requests  # позволяет парсить веб-страницы
# out = requests.get('https://mail.ru')
# print(out)

