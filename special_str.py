# -*- coding: utf-8 -*-

class Student(object):

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name:%s)' % self.name

    __repr__ = __str__


print Student('sunzhilei')

import json

d = dict(name='sun', age=31)
print type(json.dumps(d))
