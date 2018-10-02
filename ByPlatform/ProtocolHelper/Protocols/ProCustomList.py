#!/usr/bin/python
# -*- coding:utf-8 -*-
from ByPlatform.ProtocolHelper.ProtocolHelper import *
from ByPlatform.ProtocolHelper.Protocols.ProtocolBase import *
from ByPlatform.Base.OutPutHelper import *
from ByPlatform.StorageHelper.Model.CustomModel import *
import  json
class ProCustomList(ProtocolBase):
    CMD_CODE = "1030"
    def __init__(self):
        super(ProCustomList, self).__init__()
        self.Command = MessageDefine.getCommand(ProCustomList.CMD_CODE)
        self.PageIndex = 0
        self.PageSize = 3
        self.Condition = None
        pass

    def getLocalCustoms(self):
        # 转换计数变量
        self.PageIndex = int(self.PageIndex)
        self.PageSize = int(self.PageSize)

        # 返回数据清单：name  ucode  sex   age   idcard  level mobile
        customs = CustomModel.queryCustoms()

        # 去掉普通账户---和 工作人员
        for oneCm in reversed(customs):
            if oneCm.getAttribute("level") == 1000 or oneCm.getAttribute("level") == "1000":
                customs.remove(oneCm)
                continue

            #
            if oneCm.getAttribute("level") == 8888 or oneCm.getAttribute("level") == "8888":
                customs.remove(oneCm)
                continue

        conditionFliters = []
        # 根据Condition筛选----有，则需要进行
        if self.Condition and isinstance(self.Condition,dict) and len(self.Condition.keys()) > 0:
            for one in reversed(customs):
                conformCondition = True
                for oneKey in self.Condition.keys():
                    oneValues = self.Condition[oneKey]

                    try:
                        objValue = one.getAttribute(oneKey)

                        if oneValues in objValue:
                            continue

                        conformCondition = False
                        break
                    except Exception as ex:
                        continue

                if conformCondition:
                    conditionFliters.append(one)
        else:
            conditionFliters = customs

        # 对结果按照ucode排序
        conditionFliters = sorted(conditionFliters, key=lambda oneCustom: oneCustom.UCode)

        rtnDatas = []
        for index , oneCustom in enumerate(conditionFliters):
            # 跳过已经返回的数据
            if index < self.PageIndex*self.PageSize:
                continue

            # 已经有一批待返回
            if index >= (self.PageIndex + 1)*self.PageSize:
                break

            oneCustomDict = {"ucode":oneCustom.getAttribute("ucode"),"name":oneCustom.getAttribute("name"), "sex":oneCustom.getAttribute("sex"),
                             "age":oneCustom.getAttribute("age"),"idcard":oneCustom.getAttribute("idcard"),"level":oneCustom.getAttribute("level"),
                             "mobile":oneCustom.getAttribute("mobile")}
            rtnDatas.append(oneCustomDict)

        return rtnDatas

class ProCustomListAck(ProtocolBase):
    CMD_CODE = "1031"
    SUB_DICT=""
    def __init__(self):
        super(ProCustomListAck, self).__init__()
        self.Command = MessageDefine.getCommand(ProCustomListAck.CMD_CODE)
        self.CustomList = []

    def evalData(self):
        if not self.CustomList:
            self.CustomList = []

        if isinstance(self.CustomList,list):
            return

        if not isinstance(self.CustomList,str):
            self.CustomList = []
            return

        # 需要字符转换
        # eval("self.CustomList=" + self.CustomList)
        self.CustomList = json.loads(self.CustomList)
        pass


if __name__ == "__main__":
    MSG = '00000001371021000.000.000.0000005Name:caojiaju|IpAddress:192.168.1.200|HttpPort:29001|UdpPort:28001|Code:09d623c09c4711e8bca1989096c1d848'
    abc = ProtocolHelper.bindProtocol(MSG)

    abc.loadFromMsg(MSG)
    OutPutHelper.consolePrint( abc.packageMsg())


