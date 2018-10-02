#!/usr/bin/python
# -*- coding:utf-8 -*-
from ByPlatform.ProtocolHelper.ProtocolHelper import *
from ByPlatform.ProtocolHelper.Protocols.ProtocolBase import *
from ByPlatform.Base.OutPutHelper import *

class ProSetTerminalWorkTime(ProtocolBase):
    CMD_CODE = "3050"
    def __init__(self):
        super(ProSetTerminalWorkTime, self).__init__()
        self.Command = MessageDefine.getCommand(ProSetTerminalWorkTime.CMD_CODE)
        self.StartTime = None
        self.StopTime = None

class ProSetTerminalWorkTimeAck(ProtocolBase):
    CMD_CODE = "3051"
    def __init__(self):
        super(ProSetTerminalWorkTimeAck, self).__init__()
        self.Command = MessageDefine.getCommand(ProSetTerminalWorkTimeAck.CMD_CODE)
        self.Status = True


if __name__ == "__main__":
    MSG = '00000001371021000.000.000.0000005Name:caojiaju|IpAddress:192.168.1.200|HttpPort:29001|UdpPort:28001|Code:09d623c09c4711e8bca1989096c1d848'
    abc = ProtocolHelper.bindProtocol(MSG)

    abc.loadFromMsg(MSG)
    OutPutHelper.consolePrint(abc.packageMsg())


