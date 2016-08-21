# -*- coding: utf-8 -*-

input = ['adam', 'LISA', 'barT']

def transfer(x):
    list_str = []
    for num, _ in enumerate(x):
        if num == 0:
            list_str.append(_.upper())
        else:
            list_str.append(_.lower())

    return ''.join(list_str)


print map(lambda x: x.capitalize(), input)

int_input = [1,2 ,3 ,4 ,5, 10]

print reduce(lambda x, y: x*y, int_input)

class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must be 0 ~ 100!')
        self._score = value


class Screen(object):

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise ValueError('width must be an integer!')

        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise ValueError('height must be an integer!')

        self._height = value

    @property
    def resolution(self):
        return self._height * self._width

s = Screen()
s.width = 5
s.height = 10
print s.resolution