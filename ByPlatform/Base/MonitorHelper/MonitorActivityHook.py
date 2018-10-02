#!/usr/bin/python
# -*- coding:utf-8 -*-
import pythoncom, time, datetime, os
import pyHook
import threading
from ByPlatform.Base.OutPutHelper import *
from ByPlatform.Base.TimeHelper import *

__all__ = ['MonitorHelper']
LAST_TIME = None

class MonitorActivityHook(object):
    Activity_Silence = 5  # 判定是否有人使用的阈值
    Activity_Skip = 2     # 为了精度考虑， 设置不予计数的阈值
    def __init__(self,todayRecord):
        self.hookManage = pyHook.HookManager()
        self.todayRecord = todayRecord


    def haveAction(self):
        global  LAST_TIME
        # 获取当前时间
        currentTime = datetime.datetime.now()

        if not LAST_TIME:
            LAST_TIME = currentTime
            return

        # 判断当前时间是否同上一记录时间超过5秒
        # 超过5秒说明无人使用
        timeSep = currentTime - LAST_TIME
        if timeSep.seconds >= MonitorActivityHook.Activity_Silence:
            LAST_TIME = currentTime
            OutPutHelper.consolePrint(TimeHelper.timeToString(currentTime))
        #  一秒之内， 不予计数
        elif timeSep.seconds < MonitorActivityHook.Activity_Skip:
            pass
        else:  # 需要更新计数
            # OutPutHelper.consolePrint("====================>%d"%timeSep.seconds)
            LAST_TIME = currentTime
            self.todayRecord.recordtime = TimeHelper.timeToString(currentTime)
            self.todayRecord.InteractionTimes = int(self.todayRecord.InteractionTimes) + timeSep.seconds
            self.todayRecord.save()
            pass

        pass

    def onMouseEvent(self,event):
        self.haveAction()
        # 监听鼠标事件

        # 返回 True 以便将事件传给其它处理程序
        # 注意，这儿如果返回 False ，则鼠标事件将被全部拦截
        # 也就是说你的鼠标看起来会僵在那儿，似乎失去响应了
        return True

    def onKeyboardEvent(self,event):
        self.haveAction()
        # 监听键盘事件
        # currentKey = event.Key
        # 同鼠标事件监听函数的返回值
        return True
    def startMonitor(self):
        # 监听所有键盘事件
        self.hookManage.KeyDown = self.onKeyboardEvent
        # 设置键盘“钩子”
        self.hookManage.HookKeyboard()
        # 监听所有鼠标事件
        self.hookManage.MouseAll = self.onMouseEvent
        # 设置鼠标“钩子”
        self.hookManage.HookMouse()

        # 进入循环，如不手动关闭，程序将一直处于监听状态
        pythoncom.PumpMessages()

def main():
    # 创建一个“钩子”管理对象
    ttt = MonitorActivityHook()
    ttt.startMonitor()

if __name__ == "__main__":
    main()