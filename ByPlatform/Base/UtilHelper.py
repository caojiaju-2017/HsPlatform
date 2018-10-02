#!/usr/bin/python
# -*- coding:utf-8 -*-
import uuid
import re

class UtilHelper(object):
    @staticmethod
    def newUuid():
        newUuid = str(uuid.uuid1())
        newUuid = newUuid.replace('-', '')
        return newUuid

    @staticmethod
    def getScreenSize():
        # 考虑到适合windowss
        try:
            from win32api import GetSystemMetrics
            width = GetSystemMetrics(0)
            height = GetSystemMetrics(1)
        except Exception as ex:
            return (0,0)

        return  (width,height)

    @staticmethod
    def getXYrate(x,y):
        return x*1.0/y

    @staticmethod
    def isValidIdCard(idcard):
        '''
        检测身份证是否合法
        :param idcard:
        :return:
        '''
        IDCARD_REGEX = '[1-9][0-9]{14}([0-9]{2}[0-9X])?'
        if isinstance(idcard, int):
            idcard = str(idcard)

        if not re.match(IDCARD_REGEX, idcard):
            return False

        factors = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
        items = [int(item) for item in idcard[:-1]]
        copulas = sum([a * b for a, b in zip(factors, items)])
        ckcodes = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']
        return ckcodes[copulas % 11].upper() == idcard[-1].upper()

if __name__ == "__main__":
    print (UtilHelper.is_valid_idcard("370202197808283533"))