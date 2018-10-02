#!/usr/bin/python
# -*- coding:utf-8 -*-

import hashlib,os,base64,sys

class EncryptionHelper(object):
    @staticmethod
    def Md5String(srcString):
        '''
        MD5加密字符串
        :param self:
        :param srcString:
        :return:
        '''
        try:
            md5 = hashlib.md5(srcString.encode('utf-8')).hexdigest()
        except:
            md5 = hashlib.md5(srcString).hexdigest()
        return md5

    @staticmethod
    def Md5File(filepath):
        '''
        获取文件MD5码
        :param filepath:
        :return:
        '''
        if not os.path.exists(filepath):
            return None

        md5 = None
        md5file = None
        try:
            md5file = open(filepath,'rb')
            md5 = hashlib.md5(md5file.read()).hexdigest()
        except:
            pass
        finally:
            md5file.close()

        return md5

    @staticmethod
    def Base64Encode(srcString):
        '''
        Base64编码
        :param srcString:
        :return:
        '''
        maijorVersion = sys.version_info[0]

        if maijorVersion <= 2:
            return base64.b64encode(srcString)
        else:
            return base64.b64encode(srcString.encode('utf-8'))

    @staticmethod
    def Base64Decode(secretString):
        '''
        Base64解码
        :param secretString:
        :return:
        '''
        maijorVersion = sys.version_info[0]

        if maijorVersion <= 2:
            return base64.b64decode(secretString)
        else:
            return base64.b64decode(secretString.encode('utf-8'))