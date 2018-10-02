#!/usr/bin/python
# -*- coding:utf-8 -*-
import socket
import  subprocess
import  re,os,sys
import  psutil
import uuid
import pythoncom
import wmi,threading
import time
import base64

if sys.version_info[0] == 3:
    from urllib import parse
elif sys.version_info[0] == 2:
    import urllib

import struct
from ByPlatform.Base.OutPutHelper import *
from ByPlatform.Base.NetHelper.NetHelperEx import *

__all__ = ['NetHelper']
class NetHelper(object):
    def __init__(self):
        pass

    @staticmethod
    def getBroacastAddree():
        ipAddress = NetHelperEx.routingIPAddr
        maskAddress = NetHelperEx.routingIPNetmask
        broad_list = []

        subMask_split = maskAddress.split(".")
        myIp = (ipAddress + ".1").split(".")
        str_cast = ""
        for i in range(4):
            xx = (int(myIp[i]) & int(subMask_split[i])) | ((int(subMask_split[i])) ^ 255)
            str_cast = str_cast + str(xx) + "."
        broad_list.append(str_cast.rstrip("."))

        return broad_list

    @staticmethod
    def getBroacastAddreeOld():
        '''
        获取IP以及子网掩码,windows 下的命令是ipconfig,LINUX下是ifconfig,倘若再不行，我们直接用python获取ip
        :return:
        '''
        try:
            try:
                sys_cmd = subprocess.Popen('ipconfig', stdout=subprocess.PIPE)
            except:
                sys_cmd = subprocess.Popen('ifconfig', stdout=subprocess.PIPE)
        except:  #####如果用ipconfig命令无法获取到机器的ip,使用python的socket模块获取
            ip_add = socket.gethostbyname(socket.getfqdn(socket.gethostname()))
            index_ = ip_add.rfind(".")
            return [ip_add[:index_] + ".255"]

        cmd_res = sys_cmd.stdout.read()
        pattern = re.compile(r'((\d+\.){3}\d+\s)')  #########正则匹配

        maijorVersion = sys.version_info[0]

        ip_list=[]
        try:
            if maijorVersion <= 2:
                ip_list = pattern.findall(cmd_res)
            else:
                ip_list = pattern.findall( bytes.decode(cmd_res).encode("utf-8") )
        except:
            pass

        ip_add = []
        ip_add.append(NetHelper.getHostIp())
        for i in ip_list:
            if int(i[0].rstrip().split(".")[-1]) == 0:
                subMask = str(i[0])
            else:
                pass
                # ip_info = i[0][:i[0].rfind(".")]
                # if ip_info not in ip_add: ip_add.append(ip_info)
        #########计算广播地址
        broad_list = []
        for j in ip_add:
            subMask_split = subMask.split(".")
            myIp = (j + ".1").split(".")
            str_cast = ""
            for i in range(4):
                xx = (int(myIp[i]) & int(subMask_split[i])) | ((int(subMask_split[i])) ^ 255)
                str_cast = str_cast + str(xx) + "."
            broad_list.append(str_cast.rstrip("."))
        return broad_list
    @staticmethod
    def getHostIp():
        '''
        获取本机IP
        :return:
        '''
        # return "192.168.1.208"
        myname = socket.getfqdn(socket.gethostname())
        # 获取本机ip
        myaddr = socket.gethostbyname(myname)
        return myaddr

    @staticmethod
    def getHostMac():
        mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
        return ":".join([mac[e:e + 2] for e in range(0, 11, 2)])


    @staticmethod
    def IsOpen(ip, port):
        '''
        判断主机上的端口是否打开
        :param ip:
        :param port:
        :return:
        '''
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((ip, int(port)))
            s.shutdown(2)
            return True
        except:
            return False

    @staticmethod
    def IsOpenUdpPort(port):
        import os
        cmds = 'netstat -aon|findstr "%d"' % port
        output = os.popen(cmds)
        results = output.read()

        if len(results) <= 10:
            return False

        return True

    @staticmethod
    def downloadUrlImage(savepath,filename, url):
        try:
            page = urllib.urlopen(url)
            html = page.read()
            imgdata = base64.b64decode(html)

            filename = os.path.join(savepath,filename)

            file=open(filename ,'wb')
            file.write(imgdata)
            file.close()
        except:
            pass

        return filename

if __name__ == "__main__":
    OutPutHelper.consolePrint( NetHelper.getBroacastAddree())
    # OutPutHelper.consolePrint(NetHelper.getHostIp())