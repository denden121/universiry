import copy
class Row:
    def __init__(self,i,item):
        self._mas = i._mas
        self._m = i._m
        self._item = item
        self._id = i._id


    def __getitem__(self,itemm):
        if self._m*self._item+itemm-1<len(self._mas):
            return self._mas[self._m*self._item+itemm-1]
        else:
            raise Exception("Выход за пределы массива id = {}".format(self._id))

    def __setitem__(self, key, value):
        if self._m*self._item+key-1<len(self._mas):
            self._mas[self._m*self._item+key-1] = value
        else:
            raise Exception("Выход за пределы массива id = {}".format(self._id))

class Matrix:
    value = 0
    ##################################################################################
    def __init__(self, n=None, m=None, mas=None):
        # value = 0
        Matrix.value += 1
        self._id = Matrix.value
        if type(n) is Matrix:
            if m is not None or mas is not None:
                raise Exception()
            else:
                self.Create(n._n, n._m, n._mas)
        elif type(n) is int and n >= 0 and type(m) is int and m >= 0:
            self.Create(n, m, mas)
        elif type(n) is int and n >= 0:
            self.Create(n, n, m)
        elif n is None and m is None and mas is None:
            self.Create(0, 0)
        else:
            raise ValueError(f"неправильно введенные денные id = {self._id}")
        print(f"Создан объект размерами {self._n}*{self._m} и id  = {self._id}")

    def Create(self, n, m, mas=None):
        self._n = n
        self._m = m
        if n == 0 or m == 0:
            self._mas = []
        elif mas is None:
            self._mas = [0 for i in range(n * m)]
        elif type(mas) is list and len(mas) == n * m:
            self._mas = copy.copy(mas)
        else:
            raise ValueError(f"неправильно введенные денные id = {self._id}")

    def __del__(self):
        print(f"Удален объекты id = {self._id}")
    ##############################################################################################
    def isSummable(self, a):
        return self._n == a._n and self._m == a._n and(type(a) is Matrix or issubclass(a,self))

    def isMultiplicable(self, a):
        return self._m == a._n and(type(a) is Matrix or issubclass(a,self))

    ####################################################
    def getCountRows(self):
        return self._n

    def getCounColumns(self):
        return self._m

    def getId(self):
        return self._id

    #####################################################
    def __str__(self):
        temp = ''
        for i in range(self._n):
            for j in range(self._m):
                temp += str(self._mas[self._m * i + j]) + '  '
            temp += '\n'
        return temp

    def __add__(self, other):
        if self.isSummable(other):
            temp = list(self._mas[i] + other._mas[i] for i in range(self._n * self._m))
            return Matrix(self._n, self._m, temp)
        else:
            raise Exception(f"Невозможно сложить объекты id = {self._id}")

    def __sub__(self, other):
        if self.isSummable(other):
            temp = list(self._mas[i] - other._mas[i] for i in range(self._n))
            return Matrix(self._n, self._m, temp)
        else:
            raise Exception(f'Невозможно отнять объекты id = {self._id}')

    def __mul__(self, other):
        if self.isMultiplicable(other):
            countOfRows = self._n
            countOfCols = other._m
            countNewMas = self._m
            tempMas = [0 for i in range(countOfRows * countOfCols)]
            for i in range(countOfRows):
                for j in range(countOfCols):
                    sum = 0
                    for step in range(countNewMas):
                        sum += self._mas[i * self._m + step] * other._mas[step * other._m + j]
                    tempMas[i * countOfCols + j] = sum
            return Matrix(countOfRows, countOfCols, tempMas)
        elif type(other) is float or type(other) is int:
            return Matrix(self._n, self._m, [i * other for i in self._mas])
        else:
            raise Exception(f'Невозможно умножить объекты {self._id}')

    def __getitem__(self, item):
        if type(item) is int and self._n > item > -1:
            return Row(self,item)
        else:
            raise Exception("Выход за пределы массива id = {}".format(self._id))

    def __setitem__(self, key):
        if type(key) is int and self._n > key > -1:
            return Row(self, key)
        else:
            raise Exception("Выход за пределы массива id = {}".format(self._id))





