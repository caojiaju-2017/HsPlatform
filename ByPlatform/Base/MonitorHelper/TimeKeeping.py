#!/usr/bin/python
# -*- coding:utf-8 -*-
import datetime
from ByPlatform.Base.OutPutHelper import *
class TimeKeeping(object):
    '''
    函数执行计时类
    '''
    def __init__(self):
        self.__startTime = None
        self.__lastTime = None
        self.__stopTime = None


    def start(self):
        self.__startTime = datetime.datetime.now()
        self.__lastTime = self.__startTime

    def stop(self,tag,type = 0):
        '''
        计时函数
        :param tag: 使用者传入的标签
        :param type: 0 表示相对于启动时段  1 表示相对于上次打印
        :return:
        '''
        self.__stopTime = datetime.datetime.now()

        if type == 0:
            OutPutHelper.consolePrint("%s Result=> %s"%(tag,str(self.__stopTime - self.__startTime)))
        else:
            OutPutHelper.consolePrint("%s Result=> %s"% (tag,str(self.__stopTime - self.__lastTime)))

        self.__lastTime = self.__stopTime

        return (self.__stopTime - self.__startTime).seconds

    def reset(self):
        self.start()
