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