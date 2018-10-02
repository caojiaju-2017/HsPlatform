#!/usr/bin/env python
# -*- coding: utf-8 -*-

import ctypes, sys, re
import struct
from ctypes import *
from ByPlatform.Base.OutPutHelper import *
from tinydb import TinyDB, Query
from shutil import copyfile

lstMZ = {}
lstMZ["01"] = "汉族"
lstMZ["02"] = "蒙古族"
lstMZ["03"] = "回族"
lstMZ["04"] = "藏族"
lstMZ["05"] = "维吾尔族"
lstMZ["06"] = "苗族"
lstMZ["07"] = "彝族"
lstMZ["08"] = "壮族"
lstMZ["09"] = "布依族"
lstMZ["10"] = "朝鲜族"
lstMZ["11"] = "满族"
lstMZ["12"] = "侗族"
lstMZ["13"] = "瑶族"
lstMZ["14"] = "白族"
lstMZ["15"] = "土家族"
lstMZ["16"] = "哈尼族"
lstMZ["17"] = "哈萨克族"
lstMZ["18"] = "傣族"
lstMZ["19"] = "黎族"
lstMZ["20"] = "傈僳族"
lstMZ["21"] = "佤族"
lstMZ["22"] = "畲族"
lstMZ["23"] = "高山族"
lstMZ["24"] = "拉祜族"
lstMZ["25"] = "水族"
lstMZ["26"] = "东乡族"
lstMZ["27"] = "纳西族"
lstMZ["28"] = "景颇族"
lstMZ["29"] = "柯尔克孜族"
lstMZ["30"] = "土族"
lstMZ["31"] = "达翰尔族"
lstMZ["32"] = "仫佬族"
lstMZ["33"] = "羌族"
lstMZ["34"] = "布朗族"
lstMZ["35"] = "撒拉族"
lstMZ["36"] = "毛南族"
lstMZ["37"] = "仡佬族"
lstMZ["38"] = "锡伯族"
lstMZ["39"] = "阿昌族"
lstMZ["40"] = "普米族"
lstMZ["41"] = "塔吉克族"
lstMZ["42"] = "怒族"
lstMZ["43"] = "乌孜别克族"
lstMZ["44"] = "俄罗斯族"
lstMZ["45"] = "鄂温克族"
lstMZ["46"] = "德昂族"
lstMZ["47"] = "保安族"
lstMZ["48"] = "裕固族"
lstMZ["49"] = "京族"
lstMZ["50"] = "塔塔尔族"
lstMZ["51"] = "独龙族"
lstMZ["52"] = "鄂伦春族"
lstMZ["53"] = "赫哲族"
lstMZ["54"] = "门巴族"
lstMZ["55"] = "珞巴族"
lstMZ["56"] = "基诺族"
lstMZ["57"] = "其它"
lstMZ["98"] = "外国人入籍"

class IDCardData(Structure):
	DBName = "IDCards"

	def __init__(self):
		self.name = None
		self.sex = None
		self.nation = None
		self.birthday = None
		self.address = None
		self.idcard = None
		self.regorg = None
		# self.sterTerm = None
		self.startDate = None
		self.stopDate = None

		self.dbPath = "."
		self.Global_DB_Handle = None
	def setData(self,datas):
		# Name   Sex  Nation  Birthday ,Address  idcard , regOrg   sterTerm
		if not datas or len(datas) != 8:
			return
		# print (datas)
		codingName = 'utf-16'
		nameBytes = datas[0]
		sexBytes = datas[1]
		nationBytes = datas[2]
		birthdayBytes = datas[3]
		addressBytes = datas[4]
		idcardBytes = datas[5]
		regorgBytes = datas[6]
		sterTermBytes = datas[7]
		# nameBytes = b'\xf9f\xb6[y\x9a \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00 \x00'
		try:
			self.name = nameBytes.decode(codingName)
			self.sex = sexBytes.decode(codingName)
			self.nation = nationBytes.decode(codingName)
			self.birthday = birthdayBytes.decode(codingName)
			self.address = addressBytes.decode(codingName)
			self.idcard = idcardBytes.decode(codingName)
			self.regorg = regorgBytes.decode(codingName)
			sterTerm = sterTermBytes.decode(codingName)
		except Exception as ex:
			pass


		self.name = self.name.strip()
		self.sex = self.sex.strip()
		try:
			sexId = int(self.sex)
			if sexId == 0:
				self.sex = "女"
			else:
				self.sex = "男"
		except Exception as ex:
			pass

		self.nation = self.nation.strip()
		if self.nation in lstMZ:
			self.nation = lstMZ[self.nation]
		else:
			self.nation = "未知"

		self.birthday = self.birthday.strip()
		self.address = self.address.strip()
		self.idcard = self.idcard.strip()
		self.regorg = self.regorg.strip()
		self.startDate = sterTerm[:8]
		self.stopDate = sterTerm[8:]
		self.stopDate = self.stopDate.strip()
		pass

	@staticmethod
	def queryIDCardInfo(cardno,cardSaveDir):
		cardInstance = IDCardData()
		cardInstance.dbPath = cardSaveDir

		conditions = Query()
		results = cardInstance.getDBHandle().search(conditions.idcard == cardno)

		for oneCard in results:
			return oneCard


		return None

	def getDBHandle(self):
		if not self.Global_DB_Handle:
			self.Global_DB_Handle = TinyDB('%s/icards.dat'% self.dbPath)

			self.Global_Table_GlobalUrl = self.Global_DB_Handle.table("IDCard")
		return self.Global_Table_GlobalUrl

	def getFields(self):
		rtnDict = {}
		rtnDict["name"] = self.name
		rtnDict["sex"] = self.sex
		rtnDict["nation"] = self.nation
		rtnDict["birthday"] = self.birthday
		rtnDict["address"] = self.address
		rtnDict["idcard"] = self.idcard
		rtnDict["regorg"] = self.regorg
		rtnDict["startdate"] = self.startDate
		rtnDict["stopdate"] = self.stopDate

		return rtnDict

	def saveData(self, cardSaveDir):
		self.dbPath = cardSaveDir

		conditions = Query()
		results = self.getDBHandle().search(conditions.idcard == self.idcard)

		try:
			if len(results) > 0:
				conditions = Query()
				self.getDBHandle().update(fields=self.getFields(), cond=conditions.idcard == self.idcard)
			else:
				result = self.getDBHandle().insert(self.getFields())

			result = True
		except Exception as ex:
			result = False

		return result


	def printValue(self):
		OutPutHelper.consolePrint("    Current Person Name = "     + self.name)
		OutPutHelper.consolePrint("    Current Person sex = "      + self.sex)
		OutPutHelper.consolePrint("    Current Person nation = "   + self.nation)
		OutPutHelper.consolePrint("    Current Person birthday = " + self.birthday)
		OutPutHelper.consolePrint("    Current Person address = "  + self.address)
		OutPutHelper.consolePrint("    Current Person idcard = "   + self.idcard)
		OutPutHelper.consolePrint("    Current Person regorg = "   + self.regorg)
		OutPutHelper.consolePrint("    Current Person startDate = " + self.startDate)
		OutPutHelper.consolePrint("    Current Person stopDate = " + self.stopDate)
		pass

if __name__ == "__main__":

	# 保存图片
	picDir = os.path.join(os.getcwd(), "idcards")
	if not os.path.exists(picDir):
		os.mkdir(picDir)

	openFile = open("a.txt", 'rb')

	values = openFile.read(256)

	# 二进制解码
	values = struct.unpack("30s2s4s16s70s36s30s%ds" % (256 - 188), values)

	person = IDCardData()
	person.setData(values)
	person.printValue()

	# 存储数据到本地磁盘
	person.saveData("idcards")



	newCardImage = os.path.join(picDir, person.idcard + ".jpg")
	copyfile('c.bmp', newCardImage)