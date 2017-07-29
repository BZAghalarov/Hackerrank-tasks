# class Student( object):
#
#     def __init__(self, name):
#         self.name = name
#
#     def get_name(self):
#         return  self.name
#
# harry = Student("Harry Potter")
# drace = Student("Darco Malfey")
# kena = Student("Konul Tahmazova")
#
# print(kena.get_name())


class Student(object):
    '''Definition of the Student class'''

    def __init__(self, name):
        self.__name = name
        self._name = name
        self.__name_ = name
        self.__name__ = name


harry = Student('Harry Potter')
print(harry.__name_)