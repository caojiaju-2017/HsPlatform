#!/usr/bin/python
# -*- coding:utf-8 -*-
from ByPlatform.ProtocolHelper.ProtocolHelper import *
from ByPlatform.ProtocolHelper.Protocols.ProtocolBase import *

class ProTerminalList(ProtocolBase):
    CMD_CODE = "1020"
    def __init__(self):
        super(ProTerminalList, self).__init__()
        self.Command = MessageDefine.getCommand(ProTerminalList.CMD_CODE)
        pass



class ProTerminalListAck(ProtocolBase):
    CMD_CODE = "1021"
    def __init__(self):
        super(ProTerminalListAck, self).__init__()
        self.Command = MessageDefine.getCommand(ProTerminalListAck.CMD_CODE)
        self.Name = None
        self.IpAddress = None
        self.HttpPort = 0
        self.UdpPort = 0
        self.Code = None
        self.SystemName = None
        self.BitInfo = None
        self.DiskRate = None
        self.IsOpenStream = 0
        self.ServiceId = None
        self.MIp = None
        self.MMinPort = None
        self.MMaxPort = None


# if __name__ == "__main__":
#     MSG = '00000001371021000.000.000.0000005Name:caojiaju|IpAddress:192.168.1.200|HttpPort:29001|UdpPort:28001|Code:09d623c09c4711e8bca1989096c1d848'
#     abc = ProtocolHelper.bindProtocol(MSG)
#
#     abc.loadFromMsg(MSG)
#     print abc.packageMsg()


