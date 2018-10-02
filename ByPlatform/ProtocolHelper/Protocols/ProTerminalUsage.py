#!/usr/bin/python
# -*- coding:utf-8 -*-
from ByPlatform.ProtocolHelper.ProtocolHelper import *
from ByPlatform.ProtocolHelper.Protocols.ProtocolBase import *
from ByPlatform.Base.OutPutHelper import *
from ByPlatform.StorageHelper.StorageType import StorageType
from ByPlatform.StorageHelper.StorageHelper import StorageHelper
from ByPlatform.StorageHelper.ReadDataHelper import ReadDataHelper

from ByPlatform.Base.TimeHelper import TimeHelper
from datetime import datetime,timedelta
import  time
class ProTerminalUsage(ProtocolBase):
    SKIP_COMPUTER_NOT_OPEN = False
    CMD_CODE = "1160"
    def __init__(self):
        super(ProTerminalUsage, self).__init__()
        self.Command = MessageDefine.getCommand(ProTerminalUsage.CMD_CODE)
        self.StartDate = None
        self.StopDate = None

    def searchDate(self,ackHandle):
        handle = StorageHelper(None, StorageType.DevicesMonitor)
        data = ReadDataHelper()
        data.SetDBService(handle)
        handle.StartStorageServce()
        results = data.QueryRangeData(lgt_conditions=self.StartDate,ltt_condition=self.StopDate, cmp_key = "recorddate")

        # 如果没有记录
        if not results or len(results) <= 0:
            return

        # 数值计算
        startDate = TimeHelper.String2Date(self.StartDate)
        stopDate = TimeHelper.String2Date(self.StopDate)
        sepDate = (stopDate - startDate).days + 1

        for oneIndex in range (sepDate):
            timespan = timedelta(days=oneIndex)
            startDateTemp = startDate + timespan
            dataValue = TimeHelper.dateToString(startDateTemp)
            findHandle = None
            for oneResult in results:
                if oneResult["recorddate"] == dataValue:
                    findHandle= oneResult
                    break

            # 这天没开机
            if not findHandle:
                if not ProTerminalUsage.SKIP_COMPUTER_NOT_OPEN:
                    ackHandle.TotalTimes = ackHandle.TotalTimes + 8*3600
                continue

            ackHandle.TotalTimes = ackHandle.TotalTimes + 8 * 3600
            ackHandle.InteractTimes = ackHandle.InteractTimes + int(findHandle["interactiontimes"])
            pass

        ackHandle.Rates = ackHandle.InteractTimes*100.0/ackHandle.TotalTimes

class ProTerminalUsageAck(ProtocolBase):
    CMD_CODE = "1161"
    def __init__(self):
        super(ProTerminalUsageAck, self).__init__()
        self.Command = MessageDefine.getCommand(ProTerminalUsageAck.CMD_CODE)
        self.Name = None
        self.Code = None
        self.TotalTimes = 0
        self.InteractTimes = 0
        self.Rates = 0.0

if __name__ == "__main__":
    MSG = '00000001371021000.000.000.0000005Name:caojiaju|IpAddress:192.168.1.200|HttpPort:29001|UdpPort:28001|Code:09d623c09c4711e8bca1989096c1d848'
    abc = ProtocolHelper.bindProtocol(MSG)

    abc.loadFromMsg(MSG)
    OutPutHelper.consolePrint(abc.packageMsg())


