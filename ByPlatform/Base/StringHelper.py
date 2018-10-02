#!/usr/bin/python
# -*- coding:utf-8 -*-
from functools import reduce
class StringHelper(object):
    @staticmethod
    def getUnicodeStringLen(src):
        if not src:
            return 0

        length = len(src)
        utf8_length = len(src.encode('utf-8'))
        length = (utf8_length - length) / 2 + length
        return length

    @staticmethod
    def getUtf8StringLen(src):
        if not src:
            return  0
        length = len(src)
        return length

    @staticmethod
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

    @staticmethod
    def intLen(i):
        return len('%d' % i)

    @staticmethod
    def str2int(s):
        return reduce(lambda x, y:x * 10 + y, map(StringHelper.char2num, s))

    @staticmethod
    def int2dec(i):
        return i / (10 ** StringHelper.intLen(i))

    @staticmethod
    def Str2Float(s):
        return reduce(lambda x, y:x + StringHelper.int2dec(y), map(StringHelper.str2int, s.split('.')))