#!/usr/bin/python
# -*- coding:utf-8 -*-
from ByPlatform.ProtocolHelper.ProtocolHelper import *
# from ProtocolBase import *
from ByPlatform.ProtocolHelper.Protocols.ProtocolBase import *

class ProFaceBroadcast(ProtocolBase):
    CMD_CODE = "3010"
    def __init__(self):
        super(ProFaceBroadcast, self).__init__()
        self.Command = MessageDefine.getCommand(ProFaceBroadcast.CMD_CODE)
        self.UCode = None
        self.PicUrl = None
        self.Type = 1

class ProFaceBroadcastAck(ProtocolBase):
    CMD_CODE = "3011"
    def __init__(self):
        super(ProFaceBroadcastAck, self).__init__()
        self.Command = MessageDefine.getCommand(ProFaceBroadcastAck.CMD_CODE)
        pass

if __name__ == "__main__":
    ProFaceBroadcast()
    # MSG = '00000001371021000.000.000.0000005Name:caojiaju|IpAddress:192.168.1.200|HttpPort:29001|UdpPort:28001|Code:09d623c09c4711e8bca1989096c1d848'
    # abc = ProtocolHelper.bindProtocol(MSG)
    #
    # abc.loadFromMsg(MSG)
    # print abc.packageMsg()


