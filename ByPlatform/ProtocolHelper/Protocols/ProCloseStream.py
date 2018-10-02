#!/usr/bin/python
# -*- coding:utf-8 -*-
from ByPlatform.ProtocolHelper.ProtocolHelper import *
from ByPlatform.ProtocolHelper.Protocols.ProtocolBase import *
class ProCloseStream(ProtocolBase):
    CMD_CODE = "2060"
    def __init__(self):
        super(ProCloseStream, self).__init__()
        self.Command = MessageDefine.getCommand(ProCloseStream.CMD_CODE)
        pass


class ProCloseStreamtAck(ProtocolBase):
    CMD_CODE = "2061"
    def __init__(self):
        super(ProCloseStreamtAck, self).__init__()
        self.Command = MessageDefine.getCommand(ProCloseStreamtAck.CMD_CODE)
        self.Status = True


# if __name__ == "__main__":
#     MSG = '00000001371021000.000.000.0000005Name:caojiaju|IpAddress:192.168.1.200|HttpPort:29001|UdpPort:28001|Code:09d623c09c4711e8bca1989096c1d848'
#     abc = ProtocolHelper.bindProtocol(MSG)
#
#     abc.loadFromMsg(MSG)
#     print abc.packageMsg()


