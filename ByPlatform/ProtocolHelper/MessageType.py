#!/usr/bin/python
# -*- coding:utf-8 -*-
from ByPlatform.Base.OutPutHelper import *


class MessageType(object):
    ProFaceBroadcast = "3010"
    ProFaceBroadcastAck = "3011"

    ProSetTerminalWorkTime = "3050"
    ProSetTerminalWorkTimeAck = "3051"

    ProTerminalList = "1020"
    ProTerminalListAck = "1021"

    ProCustomActivitys = "1040"
    ProCustomActivitysAck = "1041"

    ProCustomList = "1030"
    ProCustomListAck = "1031"

    ProOpenStream = "2050"
    ProOpenStreamAck = "2051"

    ProCloseStream = "2060"
    ProCloseStreamAck = "2061"

    ProCustomStayStats = "1150"
    ProCustomStayStatsAck = "1151"

    ProTerminalUsage = "1160"
    ProTerminalUsageAck = "1161"

    ProCustomStats = "1170"
    ProCustomStatsAck = "1171"

    ProUpdateCustomInfoBroadcast = "3060"
    ProUpdateCustomInfoBroadcastAck = "3061"

    ProFaceImport = "3070"
    ProFaceImportAck = "3071"

    CustomActivity = "0000"

# OutPutHelper.consolePrint( type(MessageType.ProFaceBroadcast))
