#!/usr/bin/python
# -*- coding:utf-8 -*-
from CodernityDB.database import Database
from CodernityDB.hash_index import HashIndex
from  ByPlatform.StorageHelper.StorageType import StorageType
# from StorageType import *
# from WithXIndex import *
import os
from ByPlatform.Base.OutPutHelper import *


class StorageHelper(object):
    '''
    用于本地存储类,存储采用本地文档模式，存储格式为json格式，类似Mongodb
    '''
    def __init__(self ,log = None,dbname = None):
        self.__dbRoot = "datas"
        self.__dbName = dbname
        self.__DBHandle = None
        self.openFlag = False
        self.loggerHandle = log

        if self.__dbName:
            self.CreateDB()
        pass

    def GetDBHandle(self):
        if not self.__DBHandle.opened:
            self.__DBHandle.open()
        return  self.__DBHandle

    def StartStorageServce(self):
        '''
        开启存储服务
        :return:
        '''

        # 已经被初始化了，直接返回
        if self.openFlag and self.__DBHandle:
            return True,"Success"

        if not self.__dbName:
            return False, "Unset DB Name"

        # 未进行任何初始化
        if not self.__DBHandle:
            result = self.OpenDb()
            if not result or not self.__DBHandle :
                return False ,"Open LocalDB Failed"

        self.openFlag = True

        return True,"Success"

    def StopStorageServce(self):
        '''
        关闭存储服务
        :return:
        '''
        # 已经处于关闭状态
        if not self.openFlag and not self.__DBHandle:
            return True

        # 句柄有效，但状态不对
        if self.__DBHandle:
            self.__DBHandle.close()
            self.__DBHandle = None

        if self.openFlag:
            self.openFlag = False

        return True

    def GetStorageState(self):
        '''
        获取设备存储状态
        :return:字典： 当前文件、存储服务开启状态
        '''

        if self.__DBHandle:
            return self.__DBHandle.path, self.openFlag
        else:
            return None, False

    def __getModel(self):
        return StorageType.getModel(self.__dbName)

    def InsertData(self,dictDatas):
        '''
        写入数据
        :param dictDatas:
        :return:
        '''
        if not self.openFlag:
            return False,"Write Service Not Open"

        if not self.__DBHandle:
            return False, "Write Handle Exception"

        # 数据确认与验证
        dictDatas = StorageType.ValidData(self.__getModel(),dictDatas)

        try:
            self.__DBHandle.insert(dictDatas)
            return True,"Success"
        except Exception as ex:
            OutPutHelper.consolePrint(ex.message)

    def UpdateData(self,dictDatas):
        '''
        写入数据
        :param dictDatas:
        :return:
        '''
        if not self.openFlag:
            return False,"Write Service Not Open"

        if not self.__DBHandle:
            return False, "Write Handle Exception"

        # 数据确认与验证
        # dictDatas = StorageType.ValidData(self.__getModel(),dictDatas)

        try:
            self.__DBHandle.update(dictDatas)
            return True,"Success"
        except Exception as ex:
            OutPutHelper.consolePrint(ex.message)

    def CreateDB(self):
        '''
        创建nosql数据库
        :param dbName:
        :return:
        '''

        db = Database(os.path.join(self.__dbRoot,self.__dbName))

        if db.exists():
            return True,"DB Exist"
        try:
            # OutPutHelper.consolePrint("Create DB=%s, dbpath=%s"% (self.__dbName ,db.create()))
            db.create()
            # if indexname:
            #     x_ind = WithXIndex(db.path, indexname)
            #     db.add_index(x_ind)
        except Exception as ex:
            return False,"Create DB Failed"
        db.close()

        return True ,"Success"
        pass


    def OpenDb(self):
        '''
        打开当前数据库
        :param dbName:数据库名称
        :return:
        '''
        self.__DBHandle = Database(os.path.join(self.__dbRoot,self.__dbName))

        self.__DBHandle.open()

        if not self.__DBHandle.exists():
            self.__DBHandle = None
            return False,"DB Not Exist"

        try:
            self.__DBHandle.open()
        except:
            return False,"Open DB Failed"

        return True,"Success"



    def RemoveData(self,data):
        pass

    @staticmethod
    def storageDatas(dbname, datas):
        storageHandle = StorageHelper(None,dbname)
        storageHandle.StartStorageServce()
        storageHandle.InsertData(datas)
        pass
