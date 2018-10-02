#!/usr/bin/python
# -*- coding:utf-8 -*-

import os,time
from ByPlatform.Base.OutPutHelper import *
from ByPlatform.Base.FileAndDirect import *

class MysqlConnectInfo(object):
    def __init__(self):
        self.dbName = None
        self.dbIpAddress = None
        self.dbPort = 3306
        self.dbUser = "root"
        self.dbPassword = "123456"
        pass

    def loadFromDict(self,cfgDict):
        for oneKey in cfgDict:
            cmdString = "self.%s = "%oneKey + str(cfgDict[oneKey])
            try:
                exec(cmdString)
            except Exception as ex:
                pass
        pass