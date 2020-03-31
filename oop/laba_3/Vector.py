from Matrix import *


class Vector(Matrix):
    def __init__(self, n=None, mas=None):
        Matrix.__init__(self, 1, n, mas)

    def __getitem__(self, item):###
        if type(item) is int and self._n > item  -1:
            return self._mas[item]
        else:
            raise Exception("Выход за пределы массива id = {}".format(self._id))

    def __setitem__(self, key, value):
        if type(key) is int and self._n > key -1:
            self._mas[key] = value
        else:
            raise Exception("Выход за пределы массива id = {}".format(self._id))


a = Matrix(2, 2, [1, 2,3,4])
b = Vector(2,[1,2])
print(a)
print(b)
print(b*a)
b[0]=3
print(b[0])