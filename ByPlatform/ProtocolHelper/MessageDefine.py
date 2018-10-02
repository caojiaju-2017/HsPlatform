#!/usr/bin/python
# -*- coding:utf-8 -*-
from ByPlatform.ProtocolHelper.MessageType import *

class MessageDefine(object):
    SYSTEM_CMDS = []
    def __init__(self,type,name,clsName=None):
        self.cmd_code = type
        self.cls_name = clsName
        self.cmd_name = name.strip()
        pass

    @staticmethod
    def getSystemCommandList():
        MessageDefine.SYSTEM_CMDS.append(MessageDefine(MessageType.ProFaceBroadcast, '人脸识别广播          ',"ProFaceBroadcast"))
        MessageDefine.SYSTEM_CMDS.append(MessageDefine(MessageType.ProFaceBroadcastAck,'人脸识别广播          ',"ProFaceBroadcastAck"))

        MessageDefine.SYSTEM_CMDS.append(MessageDefine(MessageType.ProSetTerminalWorkTime,'设置工作时段          ',"ProSetTerminalWorkTime"))
        MessageDefine.SYSTEM_CMDS.append(MessageDefine(MessageType.ProSetTerminalWorkTimeAck,'设置工作时段          ',"ProSetTerminalWorkTimeAck"))

        MessageDefine.SYSTEM_CMDS.append(MessageDefine(MessageType.ProTerminalList, '获取终端列表          ',"ProTerminalList"))
        MessageDefine.SYSTEM_CMDS.append(MessageDefine(MessageType.ProTerminalListAck,'获取终端列表          ', "ProTerminalListAck"))

        MessageDefine.SYSTEM_CMDS.append(MessageDefine(MessageType.ProCustomActivitys,  '获取客户活动数据      ',"ProCustomActivitys"))
        MessageDefine.SYSTEM_CMDS.append(MessageDefine(MessageType.ProCustomActivitysAck,  '获取客户活动数据      ',"ProCustomActivitysAck"))

        MessageDefine.SYSTEM_CMDS.append(MessageDefine(MessageType.ProCustomList,  '获取客户列表          ',"ProCustomList"))
        MessageDefine.SYSTEM_CMDS.append(MessageDefine(MessageType.ProCustomListAck,  '获取客户列表          ',"ProCustomListAck"))

        MessageDefine.SYSTEM_CMDS.append(MessageDefine(MessageType.ProOpenStream,  '启动终端流媒体服务    ',"ProOpenStream"))
        MessageDefine.SYSTEM_CMDS.append(MessageDefine(MessageType.ProOpenStreamAck,  '启动终端流媒体服务    ',"ProOpenStreamAck"))

        MessageDefine.SYSTEM_CMDS.append(MessageDefine(MessageType.ProCloseStream,  '停止终端流媒体服务    ',"ProCloseStream"))
        MessageDefine.SYSTEM_CMDS.append(MessageDefine(MessageType.ProCloseStreamAck,  '停止终端流媒体服务    ',"ProCloseStreamAck"))

        MessageDefine.SYSTEM_CMDS.append(MessageDefine(MessageType.ProCustomStayStats,  '获取客户终端停留时间  ',"ProCustomStayStats"))
        MessageDefine.SYSTEM_CMDS.append(MessageDefine(MessageType.ProCustomStayStatsAck,  '获取客户终端停留时间  ',"ProCustomStayStatsAck"))

        MessageDefine.SYSTEM_CMDS.append(MessageDefine(MessageType.ProTerminalUsage,  '获取终端利用率',"ProTerminalUsage"))
        MessageDefine.SYSTEM_CMDS.append(MessageDefine(MessageType.ProTerminalUsageAck,  '获取终端利用率',"ProTerminalUsageAck"))

        MessageDefine.SYSTEM_CMDS.append(MessageDefine(MessageType.ProCustomStats,  '客流统计',"ProCustomStats"))
        MessageDefine.SYSTEM_CMDS.append(MessageDefine(MessageType.ProCustomStatsAck,  '客流统计',"ProCustomStatsAck"))

        MessageDefine.SYSTEM_CMDS.append(MessageDefine(MessageType.ProUpdateCustomInfoBroadcast,  '更新客户信息',"ProUpdateCustomInfoBroadcast"))
        MessageDefine.SYSTEM_CMDS.append(MessageDefine(MessageType.ProUpdateCustomInfoBroadcastAck,  '更新客户信息',"ProUpdateCustomInfoBroadcastAck"))

        MessageDefine.SYSTEM_CMDS.append(MessageDefine(MessageType.ProFaceImport,  '导入客户',"ProFaceImport"))
        MessageDefine.SYSTEM_CMDS.append(MessageDefine(MessageType.ProFaceImportAck,  '导入客户',"ProFaceImportAck"))


        # MessageDefine.SYSTEM_CMDS.append(MessageDefine(MessageType.OpenInstruct, 101, '获取业务类别          '))
        # MessageDefine.SYSTEM_CMDS.append(MessageDefine(MessageType.OpenInstruct, 105, '获取客户当前位置      '))
        # MessageDefine.SYSTEM_CMDS.append(MessageDefine(MessageType.OpenInstruct, 106, '业务与客户            '))
        # MessageDefine.SYSTEM_CMDS.append(MessageDefine(MessageType.OpenInstruct, 107, '客户与业务            '))
        # MessageDefine.SYSTEM_CMDS.append(MessageDefine(MessageType.OpenInstruct, 108, '客户与标签            '))
        # MessageDefine.SYSTEM_CMDS.append(MessageDefine(MessageType.OpenInstruct, 109, '标签与客户            '))
        # MessageDefine.SYSTEM_CMDS.append(MessageDefine(MessageType.OpenInstruct, 110, '拉取终端数据          '))
        # MessageDefine.SYSTEM_CMDS.append(MessageDefine(MessageType.OpenInstruct, 111, '冗余数据清理          '))
        # MessageDefine.SYSTEM_CMDS.append(MessageDefine(MessageType.OpenInstruct, 112, '设置业务标签          '))
        # MessageDefine.SYSTEM_CMDS.append(MessageDefine(MessageType.OpenInstruct, 113, '业务注册(SDK)         '))
        # MessageDefine.SYSTEM_CMDS.append(MessageDefine(MessageType.OpenInstruct, 114, '设置标签应用模型(SDK) '))
        # MessageDefine.SYSTEM_CMDS.append(MessageDefine(MessageType.OpenInstruct, 203, '查询终端录像列表      '))
        # MessageDefine.SYSTEM_CMDS.append(MessageDefine(MessageType.OpenInstruct, 204, '下载终端录像          '))
        # MessageDefine.SYSTEM_CMDS.append(MessageDefine(MessageType.OpenInstruct, 201, '开启终端录像          '))
        # MessageDefine.SYSTEM_CMDS.append(MessageDefine(MessageType.OpenInstruct, 202, '关闭终端录像          '))
        # MessageDefine.SYSTEM_CMDS.append(MessageDefine(MessageType.OpenInstruct, 212, '暂停服务              '))
        # MessageDefine.SYSTEM_CMDS.append(MessageDefine(MessageType.OpenInstruct, 213, '开启服务              '))
        # MessageDefine.SYSTEM_CMDS.append(MessageDefine(MessageType.OpenInstruct, 211, '配置终端语音资源      '))
        # MessageDefine.SYSTEM_CMDS.append(MessageDefine(MessageType.OpenInstruct, 302, '业务操作广播          '))
        # MessageDefine.SYSTEM_CMDS.append(MessageDefine(MessageType.OpenInstruct, 303, '设置客户标签          '))


    @staticmethod
    def getCommand(code):
        if len(MessageDefine.SYSTEM_CMDS) <= 0:
            MessageDefine.getSystemCommandList()

        codeNum = code[:4]
        for oneCmd in MessageDefine.SYSTEM_CMDS:
            if oneCmd.cmd_code == codeNum:
                return oneCmd

        return None
