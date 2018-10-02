#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys,os,shutil

class FileAndDirect(object):
    @staticmethod
    def getExternName(fileName):
        rtnExternName = os.path.splitext(fileName)[1]
        if rtnExternName == None:
            return None
        return rtnExternName.lower()

    @staticmethod
    def get_filePath_fileName_fileExt(filename):
        (filepath, tempfilename) = os.path.split(filename);
        (shotname, extension) = os.path.splitext(tempfilename);
        return filepath, shotname, extension

    @staticmethod
    def MoveFile(srcfile,dstfile):
        if not os.path.isfile(srcfile):
            pass
            # print "%s not exist!"%(srcfile)
        else:
            fpath,fname=os.path.split(dstfile)    #分离文件名和路径
            if not os.path.exists(fpath):
                os.makedirs(fpath)                #创建路径
            shutil.move(srcfile,dstfile)          #移动文件
            # print "move %s -> %s"%( srcfile,dstfile)

    @staticmethod
    def CopyFile(srcfile,dstfile):
        if not os.path.isfile(srcfile):
            pass
            # print "%s not exist!"%(srcfile)
        else:
            fpath,fname=os.path.split(dstfile)    #分离文件名和路径
            if not os.path.exists(fpath):
                os.makedirs(fpath)                #创建路径
            shutil.copyfile(srcfile,dstfile)      #复制文件


    @staticmethod
    def GetFileList(rootDir):
        rtnFileName = []
        for root, dirs, files in os.walk(rootDir):
            # print(root) #当前目录路径
            # print(dirs) #当前路径下所有子目录
            # print(files) #当前路径下所有非目录子文件
            for filename in files:
                absFileName = os.path.join(root,filename)
                absFileName = absFileName.replace("\\",os.sep)
                absFileName = absFileName.replace("/", os.sep)
                rtnFileName.append(absFileName)


        return rtnFileName

    @staticmethod
    def readAllContent(filename):
        if not os.path.exists(filename):
            return None

        f = open(filename, "r")
        rtnString = f.read()  # 读取全部内容 ，并以列表方式返回
        # rtnString = ""
        # for line in lines:
        #     rtnString = rtnString + line
        f.close()
        return rtnString

    @staticmethod
    def writeContent(filename,content):
        filename = filename
        with open(filename, 'w') as f:  # 如果filename不存在会自动创建， 'w'表示写数据，写之前会清空文件中的原有数据！
            f.write(content)
