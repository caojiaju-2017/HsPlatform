#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import inspect
from ByPlatform.Base.TimeHelper import *
from ByPlatform.Base.FileAndDirect import *
class OutPutHelper(object):
    '''
        日志类
    '''
    Logger_CallBack = None

    # 缺省输出到命令行
    Console_Logger = True

    # 标签
    Logger_Tag = "Main"

    Logger_Format = {"datetime":True, "tag":True, "filename":False, "lineno":False}
    @staticmethod
    def cmdPrint(msg):
        if sys.version_info[0] == 3:
            print(msg)
        elif sys.version_info[0] == 2:
            exec("print msg")
            # print msg
            pass

    @staticmethod
    def formatMsg (msg,upperframe,filename,tag= None):
        '''
        按顺序格式化
        :param msg:
        :return:
        '''
        # lineno

        if "lineno" in OutPutHelper.Logger_Format:
            # msg = str(upperframe.f_back.f_lineno) + " " + msg
            msg = "%04s |===>>| %s" % (str(upperframe.f_back.f_lineno) , msg)

        # filename
        if "filename" in OutPutHelper.Logger_Format:
            # filename = upperframe.f_code.co_filename
            filepath, shotname, extension = FileAndDirect.get_filePath_fileName_fileExt(filename)
            # msg = shotname + ":" + msg
            shotname = shotname[0:14]
            msg = "%014s:%s" % (shotname, msg)

        # tag
        if "tag" in OutPutHelper.Logger_Format:
            if tag:
                tag = tag[0:10]
                # msg = tag + " " + msg
                msg = "%010s | %s" % (tag, msg)
            else:
                # msg = OutPutHelper.Logger_Tag + " " + msg
                msg = "%010s | %s" % (OutPutHelper.Logger_Tag, msg)
            pass


        # datetime
        if "datetime" in OutPutHelper.Logger_Format:
            msg = TimeHelper.getCurrentTime() + "  | " + msg
            pass

        return msg
    @staticmethod
    def consolePrint(msg,tag = None):
        stack = inspect.stack()
        # the_class = stack[1][0].f_locals["self"].__class__
        fileName = stack[1][1]

        upperFrame = sys._getframe()
        msg = OutPutHelper.formatMsg(msg,upperFrame,fileName,tag)

        # 是否需要写命令行日志
        if OutPutHelper.Console_Logger:
            OutPutHelper.cmdPrint(msg)

        # 如果设置应用回调，则回调日志
        if OutPutHelper.Logger_CallBack:
            OutPutHelper.Logger_CallBack(msg)