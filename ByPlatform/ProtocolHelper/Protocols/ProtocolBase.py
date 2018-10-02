#!/usr/bin/python
# -*- coding:utf-8 -*-
from ByPlatform.ProtocolHelper.MessageDefine import *
from ByPlatform.Base.StringHelper import *
import json
class ProtocolBase(object):
    HEAD_LEN = 33
    def __init__(self):
        self.Length = 0  # 消息总长度（含头部）
        self.Command = "0000"  # 命令码
        self.DstIP = "000.000.000.000"  # 目标地址
        self.Flag = "00"
        self.Count = 0
        pass

    def loadFromMsg(self,msg):
        '''
        消息初始化当前实例
        :param msg:
        :return:
        '''
        self.loadHead(msg[:ProtocolBase.HEAD_LEN])

        # 此处需要重写
        self.__loadBody(msg[ProtocolBase.HEAD_LEN:])

        pass

    def packageMsg(self):
        '''
        消息打包函数
        :return:
        '''
        # 获取消息体
        attrList = self.getAttrList()
        bodyString = ""
        for oneAttr in attrList:
            attrValue = self.__getattribute__(oneAttr)
            valueString = None
            if isinstance(attrValue,list):
                valueString = json.dumps(attrValue)
            elif isinstance(attrValue,str):
                valueString = str(attrValue)
            elif isinstance(attrValue,dict):
                valueString = json.dumps(attrValue)
            else:
                valueString = str(attrValue)

            if not bodyString:
                bodyString = "%s:%s"%(oneAttr,valueString)
            else:
                bodyString = "%s|%s:%s" % (bodyString,oneAttr, valueString)

        # 获取消息头
        headString = "%010d" % (ProtocolBase.HEAD_LEN + StringHelper.getUtf8StringLen(bodyString))
        headString = "%s%s"%(headString,self.Command.cmd_code)
        headString = "%s%s" % (headString, self.getIp(self.DstIP))
        headString = "%s%s" % (headString, self.Flag)
        headString = "%s%02d" % (headString, len(self.getAttrList()))

        return headString + bodyString

    def getIp(self, ipaddress):
        ipInfos = ipaddress.split(".")

        return "%03d.%03d.%03d.%03d"%(int(ipInfos[0]),int(ipInfos[1]),int(ipInfos[2]),int(ipInfos[3]))

    def toIp(self,ipaddress):
        ipInfos = ipaddress.split(".")
        return "%d.%d.%d.%d" % (int(ipInfos[0]), int(ipInfos[1]), int(ipInfos[2]), int(ipInfos[3]))

    def getAttrList(self):
        '''
        获取类属性列表
        :return:
        '''
        baseAttr = ProtocolBase().__dict__.keys()

        attrList = []
        for one in  self.__dict__.keys():
            if one not in baseAttr:
                attrList.append(one)

        return attrList
        pass

    def setAttrValue(self,attrname,value):
        '''
        设置属性值
        :param attrname:
        :param value:
        :return:
        '''

        self.__setattr__(attrname,value)
        pass

    def loadHead(self,headInfo):
        '''
        从消息中装置消息头
        :param headInfo:
        :return:
        '''
        self.Length = int(headInfo[:10])
        self.Command = MessageDefine.getCommand(headInfo[10:14])
        self.DstIP = self.toIp(headInfo[14:29])
        self.Flag = headInfo[29:31]
        self.Count = int(headInfo[31:33])


    def __loadBody(self,bodyInfo):
            '''
            从消息体装在数据
            :param bodyInfo:消息体
            :return:
            '''
            attrs = self.getAttrList()

            bodyInfos = bodyInfo.split("|")

            for oneInfo in bodyInfos:
                splitPos = oneInfo.find(":")
                if splitPos < 0:
                    continue

                key = oneInfo[:splitPos]
                value = oneInfo[splitPos + 1:]

                if key in attrs:
                    self.setAttrValue(key, value)
                pass

            return