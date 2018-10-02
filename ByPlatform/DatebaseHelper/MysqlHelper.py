#!/usr/bin/python
# -*- coding:utf-8 -*-

import os,time
from ByPlatform.Base.OutPutHelper import *
from ByPlatform.Base.FileAndDirect import *
import MySQLdb

from ByPlatform.DatebaseHelper.MysqlConnectInfo import *

class MysqlHelper(object):
    def __init__(self, dbInfo):
        self.dbInfo = dbInfo
        self.connectHandle = None
    def openDb(self):
        if self.connectHandle:
            self.closeDb()

        if not self.dbInfo:
            return False
        try:
            self.connectHandle = MySQLdb.connect(self.dbInfo.dbIpAddress, self.dbInfo.dbUser,self.dbInfo.dbPassword, self.dbInfo.dbName, charset='utf8')
        except Exception as ex:
            return False

        return True

    def closeDb(self):
        if not self.connectHandle:
            return

        try:
            self.connectHandle.close()
        except Exception as ex:
            pass
        finally:
            self.connectHandle = None
        pass

    def commitChange(self,sqlLists):
        if not self.connectHandle or not sqlLists:
            return False

        try:
            cursor = self.connectHandle.cursor()

            for oneCmd in sqlLists:
                # 执行sql语句
                cursor.execute(oneCmd)
                # 提交到数据库执行
            self.connectHandle.commit()
        except:
            # Rollback in case there is any error
            self.connectHandle.rollback()
        pass

    def __buildFields(self,fds):
        rtnFields = None
        if not fds:
            return "*"


        for oneFds in fds:
            if rtnFields:
                rtnFields = rtnFields + "," + oneFds
            else:
                rtnFields = oneFds

        if not rtnFields:
            return "*"

        return  rtnFields

    def __buildConditions(self, cdicts):
        if not cdicts:
            return "1=1"

        rtnCondtion = None
        for oneKey in cdicts:
            if not rtnCondtion:
                rtnCondtion = "%s = '%s'" % (str(oneKey), str(cdicts[oneKey]))
            else:
                rtnCondtion = rtnCondtion + "and %s = '%s'" % (str(oneKey), str(cdicts[oneKey]))
        if not rtnCondtion:
            return "1=1"

        return rtnCondtion
    def queryRecords(self,tablename,fields = None,conditions= None):
        if not self.connectHandle or not tablename:
            return False

        queryFileds = self.__buildFields(fields)
        queryConditions = self.__buildConditions(conditions)

        sqlCmd = "select %s from %s where %s"%(queryFileds,tablename, queryConditions)

        # 返回查询记录
        rtnResult = []
        try:
            # 使用cursor()方法获取操作游标
            cursor = self.connectHandle.cursor()
            # 执行SQL语句
            cursor.execute(sqlCmd)

            # 获取字段名
            queryResultFields = []
            for field_desc in cursor.description:
                # print field_desc[0]
                queryResultFields.append(field_desc[0])

            # 获取所有记录列表
            results = cursor.fetchall()
            for row in results:
                oneRowDict = {}
                if len(row) != len(queryResultFields):
                    continue

                for index,oneColValue in enumerate(row):
                    oneRowDict[queryResultFields[index]] = oneColValue
                    if queryResultFields[index] == "FName":
                        print oneColValue

                rtnResult.append(oneRowDict)
        except Exception as ex:
            print "Error: unable to fecth data"

        return rtnResult

if __name__ == "__main__":
    cntInfo = MysqlConnectInfo()
    cntInfo.dbIpAddress="localhost"
    cntInfo.dbName = "erpshare"
    cntInfo.dbPassword = "123456"
    cntInfo.dbUser = "root"
    cntInfo.dbPort = 3306
    connectHandle = MysqlHelper(cntInfo)
    connectHandle.openDb()

    print connectHandle.queryRecords("table_metadata")
