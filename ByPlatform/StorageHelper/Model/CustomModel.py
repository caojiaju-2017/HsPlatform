#!/usr/bin/python
# -*- coding:utf-8 -*-

from ByPlatform.StorageHelper.StorageType import *
from ByPlatform.StorageHelper.StorageHelper import *
from ByPlatform.StorageHelper.ReadDataHelper import *

class CustomModel(object):
    def __init__(self):
        self.UCode = None
        self.recordInstance = None

    @staticmethod
    def createCustom(ucode):
        handle = StorageHelper(None, StorageType.Custom)
        data = ReadDataHelper()
        data.SetDBService(handle)
        handle.StartStorageServce()

        register = {}
        register["name"] = "未知"
        register["ucode"] = ucode
        register["sex"] = "男"
        register["age"] = 26
        register["idcard"] = ""
        register["feature"] = None
        register["photo"] = None
        register["level"] = 1000

        handle.InsertData(register)

        # # 重新查询终端文档
        # results = data.QueryData()
        # rtnHandle = None
        # for oneT in results:
        #     if oneT["conid"] == conid:
        #         rtnHandle = oneT
        #         break
        #
        handle.StopStorageServce()
        # return rtnHandle

    @staticmethod
    def queryCustoms():
        handle = StorageHelper(None, StorageType.Custom)
        data = ReadDataHelper()
        data.SetDBService(handle)
        handle.StartStorageServce()

        # 重新查询终端文档
        results = data.QueryData()

        allCustoms = []
        for oneT in results:
            oneCustom = CustomModel()
            oneCustom.recordInstance = oneT
            oneCustom.UCode = oneCustom.recordInstance["ucode"]
            allCustoms.append(oneCustom)

        handle.StopStorageServce()

        return allCustoms
    @staticmethod
    def queryCustom(ucode):
        handle = StorageHelper(None, StorageType.Custom)
        data = ReadDataHelper()
        data.SetDBService(handle)
        handle.StartStorageServce()

        conditions = {'ucode': ucode}
        # 重新查询终端文档
        results = data.QueryData(conditions = conditions)
        rtnHandle = None
        for oneT in results:
            rtnHandle = oneT
            break
        handle.StopStorageServce()

        return rtnHandle

    def delete(self):
        handle = StorageHelper(None, StorageType.Custom)
        handle.StartStorageServce()
        try:
            result = handle.GetDBHandle().delete(self.recordInstance)
            result = True
        except Exception as ex:
            result = False

        handle.StopStorageServce()

        # db.delete(doc)
        return result

    def save(self):
        handle = StorageHelper(None, StorageType.Custom)
        handle.StartStorageServce()

        # 先尝试更新
        try:
            result = handle.GetDBHandle().update(self.recordInstance)
            result = True
        except Exception as ex:
            result = False

        # 再尝试插入
        if not result:
            try:
                result = handle.GetDBHandle().insert(self.recordInstance)
                result = True
            except Exception as ex:
                result = False

        handle.StopStorageServce()

        # db.delete(doc)
        return result

    @staticmethod
    def delDoc(doc):
        handle = StorageHelper(None, StorageType.Custom)
        handle.StartStorageServce()
        try:
            result = handle.GetDBHandle().delete(doc)
            result = True
        except Exception as ex:
            result = False

        handle.StopStorageServce()

        # db.delete(doc)
        return result

    @staticmethod
    def saveDoc(doc):
        handle = StorageHelper(None, StorageType.Custom)
        handle.StartStorageServce()
        try:
            result = handle.GetDBHandle().update(doc)
            result = True
        except Exception as ex:
            result = False

        handle.StopStorageServce()

        # db.delete(doc)
        return result

    def setName(self, name):
        if not self.recordInstance:
            self.recordInstance = {}
        self.recordInstance["name"] = name

    def setUCode(self, ucode):
        if not self.recordInstance:
            self.recordInstance = {}
        self.recordInstance["ucode"] = ucode

    def setSex(self, sex):
        if not self.recordInstance:
            self.recordInstance = {}
        self.recordInstance["sex"] = sex

    def setAge(self, age):
        if not self.recordInstance:
            self.recordInstance = {}
        self.recordInstance["age"] = age

    def setIDCard(self, idcard):
        if not self.recordInstance:
            self.recordInstance = {}
        self.recordInstance["idcard"] = idcard

    def setFeature(self, feature):
        if not self.recordInstance:
            self.recordInstance = {}
        self.recordInstance["feature"] = feature

    def setPhoto(self, photo):
        if not self.recordInstance:
            self.recordInstance = {}
        self.recordInstance["photo"] = photo

    def setLevel(self, level):
        if not self.recordInstance:
            self.recordInstance = {}
        self.recordInstance["level"] = level

    def getAttribute(self,attrName):
        try:
            return self.recordInstance[attrName]
        except Exception as ex:
            return None


    @staticmethod
    def queryCustomActivity(startDate,stopDate):
        # 查询客户活动数据
        handle = StorageHelper(None, StorageType.Activity)
        data = ReadDataHelper()
        data.SetDBService(handle)
        handle.StartStorageServce()

        # 重新查询终端文档
        activitys = data.QueryRangeData(lgt_conditions=startDate, ltt_condition=stopDate,cmp_key="actdate")
        handle.StopStorageServce()

        # 查询客户数据
        handle = StorageHelper(None, StorageType.Custom)
        dataCustom = ReadDataHelper()
        dataCustom.SetDBService(handle)

        handle.StartStorageServce()

        # 查询客户数据
        customs = dataCustom.QueryData()

        # 返回客户活动数据
        # 遍历 活动数据
        #
        rtnCustomActivity = []
        for oneActivity in activitys:
            uCode = oneActivity["ucode"]
            inDate = oneActivity["actdate"]
            seconds = oneActivity["measure1"]

            # 缺省为普通账户
            uLevel = None
            userName = None
            userSex = "男"
            userAge = 26
            for oneCustom in customs:
                if not isinstance(oneCustom,dict):
                    continue
                if oneCustom["ucode"] == uCode:
                    uLevel = oneCustom["level"]
                    userName = oneCustom["name"]
                    userSex = oneCustom["sex"]
                    userAge = int(oneCustom["age"])
                    break
            if not uLevel:
                continue
            rtnCustomActivity.append({"ucode":uCode,"date":inDate,"seconds":seconds,"ulevel":uLevel,"name":userName,"sex":userSex,"age":userAge})

        handle.StopStorageServce()
        return rtnCustomActivity