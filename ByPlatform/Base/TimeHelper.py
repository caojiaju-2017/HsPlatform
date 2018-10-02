#!/usr/bin/python
# -*- coding:utf-8 -*-
import datetime

class TimeHelper(object):
    @staticmethod
    def getCurrentTime(haveSep = True):
        if haveSep:
            return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        return datetime.datetime.now().strftime('%Y%m%d%H%M%S')

    @staticmethod
    def getCurrentDate():
        return datetime.datetime.now().strftime('%Y-%m-%d')

    @staticmethod
    def timeToString(srctime):
        return srctime.strftime('%Y-%m-%d %H:%M:%S')

    @staticmethod
    def dateToString(srcdate):
        return srcdate.strftime('%Y-%m-%d')


    @staticmethod
    def String2Datetime(strTime):
        return datetime.datetime.strptime(strTime, '%Y-%m-%d %H:%M:%S')

    @staticmethod
    def String2Date(strDate):
        return datetime.datetime.strptime(strDate, '%Y-%m-%d')

