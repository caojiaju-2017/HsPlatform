#!/usr/bin/python
# -*- coding:utf-8 -*-
from ByPlatform.ProtocolHelper.ProtocolHelper import *
from ByPlatform.ProtocolHelper.Protocols.ProtocolBase import *
from ByPlatform.Base.OutPutHelper import *

class ProCustomStayStats(ProtocolBase):
    CMD_CODE = "1150"
    def __init__(self):
        super(ProCustomStayStats, self).__init__()
        self.Command = MessageDefine.getCommand(ProCustomStayStats.CMD_CODE)
        self.TCode = None
        self.StartTime = None
        self.StopTime = None

class ProCustomStayStatsAck(ProtocolBase):
    CMD_CODE = "1151"
    def __init__(self):
        super(ProCustomStayStatsAck, self).__init__()
        self.Command = MessageDefine.getCommand(ProCustomStayStatsAck.CMD_CODE)
        self.SubRecord = []


if __name__ == "__main__":
    MSG = '00000001371021000.000.000.0000005Name:caojiaju|IpAddress:192.168.1.200|HttpPort:29001|UdpPort:28001|Code:09d623c09c4711e8bca1989096c1d848'
    abc = ProtocolHelper.bindProtocol(MSG)

    abc.loadFromMsg(MSG)
    OutPutHelper.consolePrint(abc.packageMsg())


