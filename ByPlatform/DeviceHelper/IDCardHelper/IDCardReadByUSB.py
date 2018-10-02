#!/usr/bin/python
# -*- coding:utf-8 -*-
from ctypes import *
import struct,time
from shutil import copyfile

from ByPlatform.Base.OutPutHelper import *

from IDCardData import IDCardData

def startScanCard(portNum, cardSaveDir):
    lib = windll.LoadLibrary("sdtapi.dll")
    libBmp = windll.LoadLibrary("WltRS.dll")

    contrlFlag = 0

    infoLength = c_uint(0)
    while True:
        time.sleep(3)
        if contrlFlag == 0:
            result = lib.SDT_OpenPort(portNum)


            if result == 144:
                OutPutHelper.consolePrint("SDT_OpenPort Success")
            else:
                OutPutHelper.consolePrint("SDT_OpenPort Failed Return result = " + str(result))
                lib.SDT_ClosePort(portNum)
                return

        # Step1---Find
        buffer = create_string_buffer(4)
        resutl = lib.SDT_StartFindIDCard(portNum,buffer,contrlFlag)
        if resutl == 159:
            OutPutHelper.consolePrint("SDT_StartFindIDCard Success")
        else:
            OutPutHelper.consolePrint("SDT_StartFindIDCard Failed Return result = " + str(resutl))
            lib.SDT_ClosePort(portNum)
            continue

        ## Step2---SelectCard
        aaa = create_string_buffer(8)
        result2 = lib.SDT_SelectIDCard(portNum,aaa,contrlFlag)
        if result2 == 144:
            OutPutHelper.consolePrint("SDT_SelectIDCard Success")
        else:
            OutPutHelper.consolePrint("SDT_SelectIDCard Failed Return result = " + str(result2))
            lib.SDT_ClosePort(portNum)
            continue

        # Step4 --get ExternInfo读取追加地址信息
        pucAppMsg = create_string_buffer(70)
        aMsg = c_uint(0)
        result2 = lib.SDT_ReadNewAppMsg(portNum,pucAppMsg,byref(aMsg),contrlFlag)

        if result2 == 144 or result2 == 145: # 145 无追加地址信息，不算失败
            OutPutHelper.consolePrint("SDT_ReadNewAppMsg Success")
            OutPutHelper.consolePrint("    SDT_ReadNewAppMsg TextMsg Length = " + str(aMsg.value))
        else:
            OutPutHelper.consolePrint("SDT_ReadNewAppMsg Failed result1 " + str(result2))
            lib.SDT_ClosePort(portNum)
            continue


        # Step5 SDT_ReadBaseMsgToFile
        fileName1 = r"abc.txt"
        fileName2 = r"abc.jpg"


        aa1 = c_char_p(b"abc.txt")
        bb1 = c_char_p(b"abc.")

        infoLength = c_uint(0)
        b1 = c_uint(0)
        result2 = lib.SDT_ReadBaseMsgToFile(portNum,b"a.txt",byref(infoLength),b"c.wlt",byref(b1),contrlFlag)

        if result2 == 144:
            OutPutHelper.consolePrint("SDT_ReadBaseMsgToFile Success")
        else:
            OutPutHelper.consolePrint("SDT_ReadBaseMsgToFile Failed result1 " + str(result2))
            lib.SDT_ClosePort(portNum)
            continue

        # End --  关闭端口
        # if contrlFlag == 0:
        try:
            result = lib.SDT_ClosePort(portNum)
            OutPutHelper.consolePrint("SDT_ClosePort SDT_ClosePort result " + str(result))
        except:
            pass

        # 照片转换
        result2 = libBmp.GetBmp(b"c.wlt", 2)
        errorMsg = None
        if result2 == 0:
            errorMsg = "调用sdtapi.dll错误！"
        elif result2 == -1:
            errorMsg = "相片解码错误！"
        elif result2 == -2:
            errorMsg = "wlt文件后缀错误！"
        elif result2 == -3:
            errorMsg = "wlt文件打开错误！"
        elif result2 == -4:
            errorMsg = "wlt文件格式错误！"
        elif result2 == -5:
            errorMsg = "软件未授权！"
        elif result2 == -6:
            errorMsg = "设备连接错误！"

        if errorMsg:
            OutPutHelper.consolePrint("GetBmp Failed resone is  " + errorMsg)
            return

        # 解析文件
        try:
            openFile = None
            if not os.path.exists("a.txt"):
                continue

            # 保存图片
            picDir = os.path.join(os.getcwd(), cardSaveDir)
            if not os.path.exists(picDir):
                os.mkdir(picDir)


            openFile = open("a.txt",'rb')

            values = openFile.read(infoLength.value)

            # 二进制解码
            values = struct.unpack("30s2s4s16s70s36s30s%ds" % (infoLength.value - 188), values)

            person = IDCardData()
            person.setData(values)
            person.printValue()

            # 存储数据到本地磁盘
            person.saveData(cardSaveDir)



            newCardImage = os.path.join(picDir, person.idcard + ".jpg")
            copyfile('c.bmp',newCardImage)
        except Exception as ex:
            pass
        finally:
            if openFile:
                openFile.close()

    pass

#
if __name__ == "__main__":
    portNum = 1001
    cardSaveDir = "idcards"
    for index in range(1, len(sys.argv)):
        OutPutHelper.consolePrint("参数%d,   %s"% (index, sys.argv[index]))
        if index == 1:
            try:
                portNum = int(sys.argv[index])
            except Exception as ex:
                portNum = -1
                pass
        elif index == 2:
            cardSaveDir = sys.argv[index]

    if portNum <= 0:
        OutPutHelper.consolePrint("ERROR: Invalid Port Number!")
    else:
        startScanCard(portNum, cardSaveDir)
