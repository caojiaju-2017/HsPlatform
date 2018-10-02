#!/usr/bin/python
# -*- coding:utf-8 -*-

import os,time
from ByPlatform.Base.OutPutHelper import *



class ProcessHelper(object):
    @staticmethod
    def checkProcess(program_name):
        '''
        检查进程是否存在
        :param program_name:进程名称
        :return:True 存在    False 不存在
        '''
        cmdString = 'tasklist | find "%s.exe"' % program_name
        while True:
            existValue = os.system(cmdString)

            # 终止正在运行的程序
            if existValue == 0:
                return True
            else:
                return False

    @staticmethod
    def killProcess(program_name):
        cmdString = 'tasklist | find "%s.exe"' % program_name
        while True:
            existValue = os.system(cmdString)

            # 终止正在运行的程序
            if existValue == 0:
                os.system('TASKKILL /F /IM %s.exe"' % program_name)
                time.sleep(3)
            else:
                break

        return

    @staticmethod
    def startProcess(work_path, exename):

        pass
if __name__ == "__main__":
    OutPutHelper.consolePrint("ProcessHelper.checkProcess == " + str(ProcessHelper.checkProcess("mainWindow")))
    OutPutHelper.consolePrint("ProcessHelper.checkProcess == " + str(ProcessHelper.killProcess("mainWindow")))
    OutPutHelper.consolePrint("ProcessHelper.checkProcess == " + str(ProcessHelper.checkProcess("mainWindow")))