#!/usr/bin/python
# -*- coding:utf-8 -*-

import os,time
import sys
import logging, time
import logging.handlers
from ByPlatform.Base.OutPutHelper import *

rq = time.strftime('%Y%m%d', time.localtime(time.time()))
class LoggerHelper(object):
    def __init__(self):
        self.log_root = "logs"
        self.console_print = False

        try:
            os.makedirs(os.path.join(os.getcwd(),self.log_root))
        except Exception as ex:
            pass

        handlers = {
            logging.NOTSET: self.log_root + os.sep + rq + ".log",
            logging.DEBUG: self.log_root + os.sep + rq + ".log",
            logging.INFO: self.log_root + os.sep + rq + ".log",
            logging.WARNING: self.log_root + os.sep + rq + ".log",
            logging.ERROR: self.log_root + os.sep + rq + ".log",
            logging.CRITICAL: self.log_root + os.sep + rq + ".log",
        }
        self.__loggers = {}
        logLevels = handlers.keys()
        fmt = logging.Formatter('%(asctime)s [%(levelname)s]: %(message)s')

        for level in logLevels:
            #创建logger
            logger = logging.getLogger(str(level))
            logger.setLevel(level)
            #创建hander用于写日日志文件
            log_path = os.path.abspath(handlers[level])
            # fh = logging.FileHandler(log_path)
            fh = logging.handlers.TimedRotatingFileHandler(log_path, 'D', 1, 10)
            #定义日志的输出格式
            fh.setFormatter(fmt)
            fh.setLevel(level)
            #给logger添加hander
            logger.addHandler(fh)
            self.__loggers.update({level: logger})
    def info(self, message):
        self.__loggers[logging.INFO].info(message)
        if self.console_print:
            OutPutHelper.consolePrint(message)

    def error(self, message):
        self.__loggers[logging.ERROR].error(message)
        if self.console_print:
            OutPutHelper.consolePrint(message)

    def warning(self, message):
        self.__loggers[logging.WARNING].warning(message)
        if self.console_print:
            OutPutHelper.consolePrint(message)

    def debug(self, message):
        self.__loggers[logging.DEBUG].debug(message)
        if self.console_print:
            OutPutHelper.consolePrint(message)

    def critical(self, message):
        self.__loggers[logging.CRITICAL].critical(message)
        if self.console_print:
            OutPutHelper.consolePrint(message)


def WriteTerminalLog2(msg):
    # preStr = "******"
    # prtMsg = "%s %s" % (preStr, msg)
    #
    # while len(prtMsg) < 40:
    #     prtMsg = prtMsg + " "
    #
    # prtMsg = prtMsg + preStr
    # OutPutHelper.consolePrint(prtMsg)
    return


if __name__ == "__main__":
    pass