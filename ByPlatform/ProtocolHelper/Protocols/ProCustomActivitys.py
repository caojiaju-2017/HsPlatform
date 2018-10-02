#!/usr/bin/python
# -*- coding:utf-8 -*-
from ByPlatform.ProtocolHelper.ProtocolHelper import *
from ByPlatform.ProtocolHelper.Protocols.ProtocolBase import *
class ProCustomActivitys(ProtocolBase):
    CMD_CODE = "1040"
    def __init__(self):
        super(ProCustomActivitys, self).__init__()
        self.Command = MessageDefine.getCommand(ProCustomActivitys.CMD_CODE)
        self.StartDate = None
        self.StopDate = None
        self.Code  = None
        pass



class ProCustomActivitysAck(ProtocolBase):
    CMD_CODE = "1041"
    def __init__(self):
        super(ProCustomActivitysAck, self).__init__()
        self.Command = MessageDefine.getCommand(ProCustomActivitysAck.CMD_CODE)
        self.Name = None
        self.Code = None
        self.Times = 0
        self.External1 = 0
        self.External2 = 0
        self.External3 = 0
        self.External4 = 0
        self.External5 = 0


# if __name__ == "__main__":
#     MSG = '00000001371021000.000.000.0000005Name:caojiaju|IpAddress:192.168.1.200|HttpPort:29001|UdpPort:28001|Code:09d623c09c4711e8bca1989096c1d848'
#     abc = ProtocolHelper.bindProtocol(MSG)
#
#     abc.loadFromMsg(MSG)
#     print abc.packageMsg()


