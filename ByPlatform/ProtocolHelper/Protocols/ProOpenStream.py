#!/usr/bin/python
# -*- coding:utf-8 -*-
from ByPlatform.ProtocolHelper.ProtocolHelper import *
from ByPlatform.ProtocolHelper.Protocols.ProtocolBase import *
from ByPlatform.Base.OutPutHelper import *

class ProOpenStream(ProtocolBase):
    CMD_CODE = "2050"
    def __init__(self):
        super(ProOpenStream, self).__init__()
        self.Command = MessageDefine.getCommand(ProOpenStream.CMD_CODE)
        pass



class ProOpenStreamAck(ProtocolBase):
    CMD_CODE = "2051"
    def __init__(self):
        super(ProOpenStreamAck, self).__init__()
        self.Command = MessageDefine.getCommand(ProOpenStreamAck.CMD_CODE)
        self.Status = True


if __name__ == "__main__":
    MSG = '00000001371021000.000.000.0000005Name:caojiaju|IpAddress:192.168.1.200|HttpPort:29001|UdpPort:28001|Code:09d623c09c4711e8bca1989096c1d848'
    abc = ProtocolHelper.bindProtocol(MSG)

    abc.loadFromMsg(MSG)
    OutPutHelper.consolePrint(abc.packageMsg())


