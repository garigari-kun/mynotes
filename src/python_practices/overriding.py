'''
Demonstrate how class inheritance and overriding works
'''

import datetime

class Parent(object):

    def __init__(self):
        self.value = 5

    def get_value(self):
        return self.value

class Child(Parent):
    def get_value(self):
        return self.value + 1


class Logger(object):
    def log(self, message):
        print(message)

class TimestampLogger(Logger):
    def log(self, message):
        message = '{} {}'.format(datetime.datetime.now().isoformat(), message)
        super(TimestampLogger, self).log(message)


if __name__ == '__main__':
    # c = Child()
    # print(c.get_value())
    l = Logger()
    l.log('hi')
    t = TimestampLogger()
    t.log('hi')
