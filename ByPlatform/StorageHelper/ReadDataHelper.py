#!/usr/bin/python
# -*- coding:utf-8 -*-

class ReadDataHelper(object):
    def __init__(self):
        self.DataSet = None
        self.__DBObject = None
        pass
    def SetDBService(self,dbhandle):
        self.__DBObject = dbhandle

    def QueryRangeData(self,lgt_conditions=None,ltt_condition = None,cmp_key = None):
        '''
        条件查询接口
        :param lgt_conditions:值域大于等于该值
        :param ltt_condition: 值域小于等于该值
        :param cmp_key: 值域键名
        :return:
        '''
        if not cmp_key or (lgt_conditions == None and ltt_condition == None):
            return self.QueryData()
        results = self.__DBObject.GetDBHandle().all("id", with_doc=True)

        resultRtn = []
        for oneResult in results:
            # 记录没有键值，跳过
            if not oneResult.has_key(cmp_key):
                continue

            value = oneResult[cmp_key]

            # 被过滤
            if lgt_conditions and value < lgt_conditions:
                continue

            # 被过滤
            if ltt_condition and value > ltt_condition:
                continue

            resultRtn.append(oneResult)
        return resultRtn

    def QueryData(self, **conditions):
        '''
        查询本地数据---and 查询
        :param conditions:必然包含startdate，stopdate
        :return:
        '''
        if not self.__DBObject:
            return False,"DB Handle is null"

        dbh,openflag = self.__DBObject.GetStorageState()

        if not openflag or not dbh:
            return False, "Data Service is not allow"

        results = self.__DBObject.GetDBHandle().all("id",with_doc=True)
        # {'conditions': {'recorddate': '2018-08-20'}}

        resultRtn = []
        if conditions.has_key("conditions"):
            cons = conditions["conditions"]
            try:
                cons.pop("dbname")
            except:
                pass
            if not cons or len(cons.keys()) == 0:
                return  results

            for oneResult in results:
                valid = True
                for oneKey in cons.keys():
                    key = oneKey
                    value = cons[key]

                    if not oneResult.has_key(key):
                        continue

                    objValue = oneResult[key]
                    if objValue != value:
                        valid = False
                        break

                if valid:
                    resultRtn.append(oneResult)
            return  resultRtn
        else:
            for oneRecord in results:
                resultRtn.append(oneRecord)
            return resultRtn





