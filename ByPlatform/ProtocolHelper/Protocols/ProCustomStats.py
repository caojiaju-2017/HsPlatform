#!/usr/bin/python
# -*- coding:utf-8 -*-
from ByPlatform.ProtocolHelper.ProtocolHelper import *
from ByPlatform.ProtocolHelper.Protocols.ProtocolBase import *
from ByPlatform.Base.OutPutHelper import *

from ByPlatform.StorageHelper.StorageHelper import StorageHelper
from ByPlatform.StorageHelper.StorageType import StorageType
from ByPlatform.StorageHelper.ReadDataHelper import ReadDataHelper

class ProCustomStats(ProtocolBase):
    CMD_CODE = "1170"
    def __init__(self):
        super(ProCustomStats, self).__init__()
        self.Command = MessageDefine.getCommand(ProCustomStats.CMD_CODE)
        self.StartDate = None
        self.StopDate = None

    def queryDatas(self):
        handle = StorageHelper(None, StorageType.Activity)
        data = ReadDataHelper()
        data.SetDBService(handle)
        handle.StartStorageServce()
        results = data.QueryRangeData(lgt_conditions=self.StartDate, ltt_condition=self.StopDate, cmp_key="actdate")
        # results = data.QueryData()


        rtnDict = {}

        # 剔除重复项
        multiIds = []
        for one in results:
            # OutPutHelper.consolePrint( one)
            mutilKey = one["ucode"] + one["actdate"]
            if mutilKey in multiIds:
                continue

            if rtnDict.has_key(one["actdate"]):
                curValue = rtnDict[one["actdate"]]

                curValue["count"] = curValue["count"] + 1

                existUCode = curValue["customids"]
                existUCode.append(one["ucode"])
                curValue["customids"] = existUCode

                rtnDict[one["actdate"]] = curValue
            else:
                rtnDict[one["actdate"]] = {"count":1 , "customids":[one["ucode"]]}

            multiIds.append(mutilKey)

        return rtnDict


    @staticmethod
    def statCustomFlow(startdate,stopdate):
        handle = ProCustomStats()
        handle.StartDate = startdate
        handle.StopDate = stopdate
        return  handle.queryDatas()


class ProCustomStatsAck(ProtocolBase):
    CMD_CODE = "1171"
    def __init__(self):
        super(ProCustomStatsAck, self).__init__()
        self.Command = MessageDefine.getCommand(ProCustomStatsAck.CMD_CODE)
        self.IPAddress = None
        self.HttpPort = None


if __name__ == "__main__":
    MSG = '00000001371021000.000.000.0000005Name:caojiaju|IpAddress:192.168.1.200|HttpPort:29001|UdpPort:28001|Code:09d623c09c4711e8bca1989096c1d848'
    abc = ProtocolHelper.bindProtocol(MSG)

    abc.loadFromMsg(MSG)
    OutPutHelper.consolePrint(abc.packageMsg())


