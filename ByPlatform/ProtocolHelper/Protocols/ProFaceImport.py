#!/usr/bin/python
# -*- coding:utf-8 -*-
from ByPlatform.ProtocolHelper.ProtocolHelper import *
# from ProtocolBase import *
from ByPlatform.ProtocolHelper.Protocols.ProtocolBase import *

class ProFaceImport(ProtocolBase):
    CMD_CODE = "3070"
    def __init__(self):
        super(ProFaceImport, self).__init__()
        self.Command = MessageDefine.getCommand(ProFaceImport.CMD_CODE)
        self.Name = None
        self.Age = None
        self.Sex = None
        self.IdCard = None
        self.Mobile = None
        self.Level = None
        self.UCode = None
        self.PicUrl = None

class ProFaceImportAck(ProtocolBase):
    CMD_CODE = "3071"
    def __init__(self):
        super(ProFaceImportAck, self).__init__()
        self.Command = MessageDefine.getCommand(ProFaceImportAck.CMD_CODE)
        pass

if __name__ == "__main__":
    ProFaceBroadcast()
    # MSG = '00000001371021000.000.000.0000005Name:caojiaju|IpAddress:192.168.1.200|HttpPort:29001|UdpPort:28001|Code:09d623c09c4711e8bca1989096c1d848'
    # abc = ProtocolHelper.bindProtocol(MSG)
    #
    # abc.loadFromMsg(MSG)
    # print abc.packageMsg()


