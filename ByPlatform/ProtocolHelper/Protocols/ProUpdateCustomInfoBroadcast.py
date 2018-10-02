#!/usr/bin/python
# -*- coding:utf-8 -*-
from ByPlatform.ProtocolHelper.ProtocolHelper import *
# from ProtocolBase import *
from ByPlatform.ProtocolHelper.Protocols.ProtocolBase import *

class ProUpdateCustomInfoBroadcast(ProtocolBase):
    CMD_CODE = "3060"
    def __init__(self):
        super(ProUpdateCustomInfoBroadcast, self).__init__()
        self.Command = MessageDefine.getCommand(ProUpdateCustomInfoBroadcast.CMD_CODE)
        self.UCode = None
        self.Name = None
        self.Age = 0
        self.Sex = "男"
        self.IDCard = None
        self.Mobile = None
        self.Level = 1000
        self.Type = -1
    def UpdateCustomInfo(self):
        OutPutHelper.consolePrint("my terminal UpdateCustomInfo")
        # 查询
        # 查询客户数据
        handle = StorageHelper(None, StorageType.Custom)
        dataCustom = ReadDataHelper()
        dataCustom.SetDBService(handle)

        handle.StartStorageServce()

        # 查询客户数据
        customs = dataCustom.QueryData(conditions={"ucode":self.UCode})

        # 返回客户活动数据
        # 遍历 活动数据
        #
        customDoc = None
        for oneCustom in customs:
            if not isinstance(oneCustom, dict):
                continue
            customDoc = oneCustom
            break

        if not customDoc:
            return

        try:
            customDoc["name"] = self.Name
            customDoc["sex"] = self.Sex
            customDoc["age"] = self.Age
            customDoc["idcard"] = self.IDCard
            customDoc["level"] = self.Level
            customDoc["mobile"] = self.Mobile

            if int(self.Type) == 0:
                result = handle.GetDBHandle().delete(customDoc)
            else:
                result = handle.GetDBHandle().update(customDoc)
            result = True
        except Exception as ex:
            result = False

        handle.StopStorageServce()
        # 更新数据库

        #
        pass

class ProUpdateCustomInfoBroadcastAck(ProtocolBase):
    CMD_CODE = "3061"
    def __init__(self):
        super(ProUpdateCustomInfoBroadcastAck, self).__init__()
        self.Command = MessageDefine.getCommand(ProUpdateCustomInfoBroadcastAck.CMD_CODE)
        self.Code = None
        pass

if __name__ == "__main__":
    ProFaceBroadcast()
    # MSG = '00000001371021000.000.000.0000005Name:caojiaju|IpAddress:192.168.1.200|HttpPort:29001|UdpPort:28001|Code:09d623c09c4711e8bca1989096c1d848'
    # abc = ProtocolHelper.bindProtocol(MSG)
    #
    # abc.loadFromMsg(MSG)
    # print abc.packageMsg()


