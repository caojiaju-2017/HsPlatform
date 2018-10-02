#!/usr/bin/python
# -*- coding:utf-8 -*-

from ByPlatform.ProtocolHelper.Protocols.ProtocolBase import ProtocolBase
from ByPlatform.ProtocolHelper.Protocols.ProTerminalList import *
from ByPlatform.ProtocolHelper.Protocols.ProFaceBroadcast import *
from ByPlatform.ProtocolHelper.Protocols.ProCloseStream import *
from ByPlatform.ProtocolHelper.Protocols.ProCustomActivitys import *
from ByPlatform.ProtocolHelper.Protocols.ProCustomList import *
from ByPlatform.ProtocolHelper.Protocols.ProCustomStats import *
from ByPlatform.ProtocolHelper.Protocols.ProCustomStayStats import *
from ByPlatform.ProtocolHelper.Protocols.ProOpenStream import *
from ByPlatform.ProtocolHelper.Protocols.ProSetTerminalWorkTime import *
from ByPlatform.ProtocolHelper.Protocols.ProTerminalUsage import *
from ByPlatform.ProtocolHelper.Protocols.ProFaceImport import *
from  ByPlatform.ProtocolHelper.Protocols.ProUpdateCustomInfoBroadcast import *

class ProtocolHelper(object):
    def __init__(self):
        pass

    @staticmethod
    def GetLastMsg(msgContent):
        '''
        从消息字符中分离第一条
        :param msgContent:
        :return:第一个参数为剩下的消息体，第二个返回值为当前消息生成对象
        '''
        if not msgContent:
            return  "",None

        msgContent = msgContent.strip()

        if len(msgContent) <= 0:
            return "",None

        # 提取长度
        currentMsg = None
        firstLen = 0
        try:
            firstLen = int(msgContent[:10])
            currentMsg = msgContent[:firstLen]
        except:
            # 消息体存在问题， 智能愈合
            return "",None

        currentCommand = ProtocolBase()
        currentCommand.loadFromMsg(currentMsg)
        return msgContent[firstLen:],currentCommand

    @staticmethod
    def bindProtocol(msg):
        '''
        消息初始化当前实例
        :param msg:
        :return:
        '''
        base = ProtocolBase()
        base.loadHead(msg[:ProtocolBase.HEAD_LEN])

        if not base:
            return None

        return  eval(base.Command.cls_name + "()")