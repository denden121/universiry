class Fraction:
    # проверка знака в дроби
    def check_sign(self):
        if self.top < 0 and self.bottom < 0:
            self.bottom, self.top = abs(self.bottom), abs(self.top)
        elif self.top > 0 and self.bottom < 0:
            self.top, self.bottom = -self.top, -self.bottom

    # нахождение максимального общего делителя
    @staticmethod
    def find_divider(a, b):
        while a != 0 and b != 0:
            if a > b:
                a = a % b
            else:
                b = b % a
        return a + b

    # коструктор
    def __init__(self, top=1, bottom=1):  # по умолчанию будет 1
        if type(top) is int and type(bottom) is int and bottom != 0:  # проверяю нет ли деления на ноль
            if top == 0:  # если числитель равен нулю занудяю дробь
                self.top = 0
                self.bottom = 0
            else:
                divider = Fraction.find_divider(abs(top), abs(bottom))  # нахожу общий наибольший делитель
                self.top, self.bottom = top, bottom
                self.top //= divider
                self.bottom //= divider
                print(f'Создана дробь {self.top}/{self.bottom}.')
        else:
            raise Exception("Не правильно введены данные.")

    def __str__(self):
        return f'{self.top} / {self.bottom}'

    # диструктор
    def __del__(self):
        print(f'Удалена дробь {self.top}/{self.bottom}.')

    # перегрузка операторов
    def __neg__(self):  # определение унарного оператора -
        self.top = self.top * -1

    def __add__(self, other):
        if type(other) is Fraction:
            return Fraction((self.top * other.bottom + other.top * self.bottom), self.bottom * other.bottom)
        elif type(other) is int:
            return Fraction(self.top + (other * self.bottom), self.bottom)
        else:
            raise Exception('Невозможно сложить')

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        return self + other

    def __sub__(self, other):
        if type(other) is Fraction:
            return Fraction((self.top * other.bottom - other.top * self.bottom), self.bottom * other.bottom)
        elif type(other) is int:
            return Fraction(self.top - (other * self.bottom), self.bottom)
        else:
            raise Exception('Невозможно отнять')

    def __rsub__(self, other):
        return self - other

    def __isub__(self, other):
        return self - other

    def __mul__(self, other):
        if type(other) is Fraction:
            return Fraction(self.top * other.top, self.bottom * other.bottom)
        elif type(other) is int:
            return Fraction(self.top * other, self.bottom)
        else:
            raise Exception('Невозможно умножить')

    def __rmul__(self, other):
        return self * other

    def __imul__(self, other):
        return self * other

    def __truediv__(self, other):
        if type(other) is Fraction:
            return Fraction(self.top * other.bottom, self.bottom * other.top)
        elif type(other) is int:
            return Fraction(self.top, self.bottom * other)
        else:
            raise Exception('Невозможно разделить')

    def __rtruediv__(self, other):
        return self / other

    def __itruediv__(self, other):
        return self / other

    # декомпазиция неправильной дроби
    def decomposition(self):
        if self.top > self.bottom:
            print(f'{self.top // self.bottom} and {self.top % self.bottom}/{self.bottom}')
        else:
            print(self)


a = Fraction(3, 5)
b = Fraction(7, 15)
c = 5 + b
print(c)
c = b + 5
print(c)
c = a + b
print(c)
c = b + a
print(c)
c += b
print(c)
c += 5
c.decomposition()
