#!/usr/bin/python
# -*- coding:utf-8 -*-
import serial
import  time

from ByPlatform.Base.OutPutHelper import *

class ComHelper(object):
    def __init__(self, comId, boardrate = 19200 ,callBackFunction = None):
        self.comId = "Com%d"%(int(comId) + 1)
        self.boardrate = boardrate
        self.callbackFunction = callBackFunction
        self.commandLength = 4  #指令长度，字节
        self.__comConnectHandle = None
        self.abortFlag = False
    def readData(self):
        while not self.abortFlag:
            response = self.__comConnectHandle.read(self.commandLength)
            if len(response) < self.commandLength :
                time.sleep(1)
                continue
            response = self.convert_hex(response)

            if self.callbackFunction:
                self.callbackFunction(response)

            time.sleep(0.1)

    def closeCom(self):
        try:
            self.__comConnectHandle.close()
            self.abortFlag = True
        except:
            pass
        pass

    def openCom(self):
        try:
            self.abortFlag = False
            self.__comConnectHandle = serial.Serial(self.comId, self.boardrate, timeout=1)
        except Exception as ex:
            return False

        return True

    # 转成16进制的函数
    def convert_hex(self, string):
        res = []
        result = []
        for item in string:
            res.append(item)
        for i in res:
            result.append(hex(i))
        return result