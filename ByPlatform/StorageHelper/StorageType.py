#!/usr/bin/python
# -*- coding:utf-8 -*-

class StorageType(object):
    Custom   = 'Custom'    # 记录客户数据
    Service  = 'Service'   # 记录当前网点业务类型
    Labels   = 'Labels'    # 标签定义
    Activity = 'Activity'  # 客户活动记录表
    CustomALabels = 'CustomALabels'
    ServiceALables =  'ServiceALables'
    Devices = "Devices"
    DevicesMonitor = "DevicesMonitor"
    RelationActionCfg = "RelationActionCfg"

    @staticmethod
    def getRelationActionCfgModel():
        '''
        获取客户模型定义
        :return:
        '''
        rtnModel = []
        rtnModel.append({"name": "conid", "type": "String"          , "alias": "条件ID","default":"未知","isindex":0})
        rtnModel.append({"name": "wayid", "type": "String"          , "alias": "联动方式", "default": "", "isindex": 0})
        rtnModel.append({"name": "isloop", "type": "String"         , "alias": "是否循环","default":"","isindex":0})
        rtnModel.append({"name": "resource", "type": "String"     , "alias": "资源", "default": "", "isindex": 0})
        return rtnModel

    @staticmethod
    def getDevicesMonitorModel():
        '''
        获取客户模型定义
        :return:
        '''
        rtnModel = []
        rtnModel.append({"name": "code", "type": "String", "alias": "记录编码", "default": "", "isindex": 0})
        rtnModel.append({"name": "recorddate", "type": "String", "alias": "记录日期","default":"","isindex":0})
        rtnModel.append({"name": "recordtime", "type": "String", "alias": "最后登记时间", "default": "", "isindex": 0})
        rtnModel.append({"name": "interactiontimes", "type": "String", "alias": "互动总时间", "default": "", "isindex": 0})
        return rtnModel

    @staticmethod
    def getDevicesModel():
        '''
        获取客户模型定义
        :return:
        '''
        rtnModel = []
        rtnModel.append({"name": "name", "type": "String", "alias": "名称","default":"未知","isindex":0})
        rtnModel.append({"name": "code", "type": "String", "alias": "设备编码", "default": "", "isindex": 0})
        rtnModel.append({"name": "scode", "type": "String", "alias": "业务编码","default":"","isindex":0})

        rtnModel.append({"name": "ipaddress", "type": "String", "alias": "IP地址(IP)", "default": "", "isindex": 0})
        rtnModel.append({"name": "minport", "type": "String", "alias": "小端口", "default": "", "isindex": 0})
        rtnModel.append({"name": "maxport", "type": "String", "alias": "大端口", "default": "", "isindex": 0})
        return rtnModel

    @staticmethod
    def getCustomModel():
        '''
        获取客户模型定义
        :return:
        '''
        rtnModel = []
        rtnModel.append({"name": "name", "type": "String", "alias": "姓名","default":"未知","isindex":0})
        rtnModel.append({"name": "ucode", "type": "String", "alias": "客户代码", "default": "未知", "isindex": 0})
        rtnModel.append({"name": "sex", "type": "String", "alias": "性别","default":"男","isindex":0})
        rtnModel.append({"name": "age", "type": "Int", "alias": "年龄","default":"20","isindex":0})
        rtnModel.append({"name": "idcard", "type": "String", "alias": "身份证","default":"******************","isindex":0})
        rtnModel.append({"name": "feature", "type": "String", "alias": "特征","default":"","isindex":0})
        rtnModel.append({"name": "photo", "type": "String", "alias": "照片","default":"","isindex":0})
        rtnModel.append({"name": "level", "type": "String", "alias": "级别", "default": "", "isindex": 0})
        rtnModel.append({"name": "mobile", "type": "String", "alias": "电话", "default": "", "isindex": 0})
        return rtnModel

    @staticmethod
    def getServiceModel():
        '''
        获取业务模型定义
        :return:
        '''
        rtnModel = []
        rtnModel.append({"name": "name", "type": "String", "alias": "名称","default":"未知","isindex":0})
        rtnModel.append({"name": "keyword1", "type": "String", "alias": "关键词1","default":"","isindex":0})
        rtnModel.append({"name": "keyword2", "type": "String", "alias": "关键词2","default":"","isindex":0})
        rtnModel.append({"name": "keyword3", "type": "String", "alias": "关键词3","default":"","isindex":0})
        rtnModel.append({"name": "info", "type": "String", "alias": "描述","default":"","isindex":0})

        return rtnModel

    @staticmethod
    def getLabelsModel():
        '''
        获取标签模型定义
        :return:
        '''
        rtnModel = []
        rtnModel.append({"name": "name", "type": "String", "alias": "名称","default":"未知","isindex":0})
        rtnModel.append({"name": "model1", "type": "Calc", "alias": "计算模型1","default":"","isindex":0})
        rtnModel.append({"name": "model2", "type": "Calc", "alias": "计算模型2","default":"","isindex":0})
        rtnModel.append({"name": "model3", "type": "Calc", "alias": "计算模型3","default":"","isindex":0})

        return rtnModel

    @staticmethod
    def getActivityModel():
        '''
        获取标签模型定义
        :return:
        '''
        rtnModel = []
        rtnModel.append({"name": "ucode", "type": "String", "alias": "关联客户", "default": "", "isindex": 0})
        rtnModel.append({"name": "name", "type": "String", "alias": "活动名","default":"未知","isindex":0})
        rtnModel.append({"name": "code", "type": "String", "alias": "活动代码","default":"","isindex":0})
        rtnModel.append({"name": "servicecode", "type": "String", "alias": "关联业务", "default": "","isindex":0})
        rtnModel.append({"name": "actdate", "type": "String", "alias": "发生日期", "default": "", "isindex": 0})
        rtnModel.append({"name": "acttime", "type": "String", "alias": "发生时间","default":"","isindex":0})
        rtnModel.append({"name": "measure1", "type": "String", "alias": "活动计量1","default":"","isindex":0})
        rtnModel.append({"name": "measure2", "type": "String", "alias": "活动计量2", "default": "","isindex":0})
        rtnModel.append({"name": "measure3", "type": "String", "alias": "活动计量3", "default": "","isindex":0})
        rtnModel.append({"name": "measure4", "type": "String", "alias": "活动计量4", "default": "","isindex":0})
        rtnModel.append({"name": "measure5", "type": "String", "alias": "活动计量5", "default": "","isindex":0})

        return rtnModel

    @staticmethod
    def getCustomALabelsModel():
        '''
        获取标签模型定义
        :return:
        '''
        rtnModel = []
        rtnModel.append({"name": "ucode", "type": "String", "alias": "客户代码","default":"","isindex":0})
        rtnModel.append({"name": "lcode", "type": "String", "alias": "标签代码", "default": "","isindex":0})
        return rtnModel

    @staticmethod
    def getServiceALablesModel():
        '''
        获取标签模型定义
        :return:
        '''
        rtnModel = []
        rtnModel.append({"name": "scode", "type": "String", "alias": "业务代码","default":"","isindex":0})
        rtnModel.append({"name": "lcode", "type": "String", "alias": "标签代码", "default": "","isindex":0})
        return rtnModel


    @staticmethod
    def getModel(dbname):
        if dbname == StorageType.Service:
            return StorageType.getServiceModel()
        elif dbname == StorageType.Custom:
            return StorageType.getCustomModel()
        elif dbname == StorageType.Labels:
            return StorageType.getLabelsModel()
        elif dbname == StorageType.Activity:
            return StorageType.getActivityModel()
        elif dbname == StorageType.CustomALabels:
            return StorageType.getCustomALabelsModel()
        elif dbname == StorageType.ServiceALables:
            return StorageType.getServiceALablesModel()
        elif dbname == StorageType.Devices:
            return StorageType.getDevicesModel()
        elif dbname == StorageType.DevicesMonitor:
            return StorageType.getDevicesMonitorModel()
        elif dbname == StorageType.RelationActionCfg:
            return StorageType.getRelationActionCfgModel()

    @staticmethod
    def getModelIndex(dbname):
        attrList = []
        if dbname == StorageType.Service:
            attrList = StorageType.getServiceModel()
        elif dbname == StorageType.Custom:
            attrList = StorageType.getCustomModel()
        elif dbname == StorageType.Labels:
            attrList = StorageType.getLabelsModel()
        elif dbname == StorageType.Activity:
            attrList = StorageType.getActivityModel()
        elif dbname == StorageType.CustomALabels:
            attrList = StorageType.getCustomALabelsModel()
        elif dbname == StorageType.ServiceALables:
            attrList = StorageType.getServiceALablesModel()

        return []
    @staticmethod
    def ValidData(models,datas):
        keyList =[]
        for oneAttr in models:
            name = oneAttr["name"]
            keyList.append(name)
            default = oneAttr["default"]
            # 检查当前属性是否在数据内
            if datas.has_key(name):
                continue
            datas[name] = default


        waitRemoveKey = []
        for key in datas:
            if key in keyList:
                continue

            waitRemoveKey.append(key)

        # 清退数据
        for oneKey in waitRemoveKey:
            datas.pop(oneKey)

        return datas