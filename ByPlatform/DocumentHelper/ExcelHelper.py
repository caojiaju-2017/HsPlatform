#!/usr/bin/python
# -*- coding:utf-8 -*-

import os,time
from ByPlatform.Base.OutPutHelper import *
from ByPlatform.Base.FileAndDirect import *
import win32com.client as win32
from ByPlatform.Base.UtilHelper import *

class ExcelHelper(object):
    def __init__(self, excelFile):
        self.__excelFile = excelFile
        pass

    def readData(self,sheetname,rowStart = 0, rowStop = -1, colStart = 0 , colStop = -1):
        '''
        数据读取
        :param rowStart:开始行
        :param rowStop:结束行
        :param colStart:开始列
        :param colStop:结束列
        :return:[{},{},{}]
        '''
        if not self.__excelFile:
            return []

        if not os.path.exists(self.__excelFile):
            return []

        excel = win32.Dispatch('Excel.Application')  # 获取Excel
        excel.Visible = True
        wb = excel.Workbooks.open(self.__excelFile)
        ws = wb.Worksheets(sheetname)

        # ws.Range('C2').value = 10

        # 保存为图片
        # ws.Range('A1:D10').CopyPicture()
        # ws.Paste(ws.Range('G1'))
        # ws.Shapes('图片 1').copy()
        # img = ImageGrab.grabclipboard()
        # img.save('D:\\article_data\\图片1.png')

        rtnAllDatas = []
        for index in range(rowStart,rowStop,1):
            oneRow = {}
            for colInx in range(colStart,colStop,1):
                ValueTmp = ws.Cells(index,colInx).Value
                oneRow[colInx] = ValueTmp
            rtnAllDatas.append(oneRow)



        wb.Close(SaveChanges=0)

        return rtnAllDatas

if __name__ == "__main__":
    from ByPlatform.DatebaseHelper.MysqlConnectInfo import *
    from ByPlatform.DatebaseHelper.MysqlHelper import *
    cntInfo = MysqlConnectInfo()
    cntInfo.dbIpAddress="localhost"
    cntInfo.dbName = "erpshare"
    cntInfo.dbPassword = "123456"
    cntInfo.dbUser = "root"
    cntInfo.dbPort = 3306
    connectHandle = MysqlHelper(cntInfo)
    connectHandle.openDb()

    fieldsTables =  connectHandle.queryRecords("table_metadata")

    fieldsTables = sorted(fieldsTables, key=lambda oneRow: oneRow["FIndex"])

    picDir = os.path.join(os.getcwd(), "111.xlsx")
    if not os.path.exists(picDir):
        pass
    else:
        results = ExcelHelper(picDir).readData(u"123",4,272,1,17)

        pass

    sqlCommand = []
    for oneRecord in results:
        currentRowCode = UtilHelper.newUuid()
        oneSql = None
        fields = None
        values = None
        for index , fd in enumerate(fieldsTables):
            # if not fields:
            #     fields = fd["FName"]
            # else:
            #     fields = "%s,%s"%(fields,fd["FName"])

            # # value
            # if not values:
            #     values = "'%s'" % oneRecord[index]
            # else:
            #     values = "'%s','%s'" % (values,oneRecord[index])

            oneSql = "insert into erp_services(code, fname, fvalue) values('%s','%s','%s')" % \
                     (currentRowCode,fd["FName"],oneRecord[index + 1])

            # OutPutHelper.consolePrint(oneSql)
            sqlCommand.append(oneSql)

    connectHandle.commitChange(sqlCommand)