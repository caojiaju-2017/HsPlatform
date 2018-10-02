from distutils.core import setup
setup(
name='BYPlatform',
version='1.0',
description='Boyuan Smart Platform',
author='caojiaju',
author_email='caojiaju@by-creat.com',
url='http://www.by-creat.com',
py_modules=[
            'ByPlatform.__init__',
            'ByPlatform.StorageHelper.ReadDataHelper',
            'ByPlatform.StorageHelper.StorageHelper',
            'ByPlatform.StorageHelper.StorageType',
            'ByPlatform.StorageHelper.WithXIndex',
            'ByPlatform.StorageHelper.Model.CustomModel',

            'ByPlatform.LoggerHelper.LoggerHelper',

            'ByPlatform.EncryptionHelper.EncryptionHelper',

            'ByPlatform.ProtocolHelper.MessageDefine',
            'ByPlatform.ProtocolHelper.MessageType',
            'ByPlatform.ProtocolHelper.ProtocolHelper',

            'ByPlatform.DeviceHelper.ComHelper',
            'ByPlatform.DeviceHelper.IDCardHelper.IDCardData',

            'ByPlatform.ProtocolHelper.Protocols.ProtocolBase',
            'ByPlatform.ProtocolHelper.Protocols.ProCloseStream',
            'ByPlatform.ProtocolHelper.Protocols.ProCustomActivitys',
            'ByPlatform.ProtocolHelper.Protocols.ProCustomList',
            'ByPlatform.ProtocolHelper.Protocols.ProCustomStats',
            'ByPlatform.ProtocolHelper.Protocols.ProCustomStayStats',
            'ByPlatform.ProtocolHelper.Protocols.ProFaceBroadcast',
            'ByPlatform.ProtocolHelper.Protocols.ProOpenStream',
            'ByPlatform.ProtocolHelper.Protocols.ProSetTerminalWorkTime',
            'ByPlatform.ProtocolHelper.Protocols.ProTerminalList',
            'ByPlatform.ProtocolHelper.Protocols.ProTerminalUsage',
            'ByPlatform.ProtocolHelper.Protocols.ProUpdateCustomInfoBroadcast',
            'ByPlatform.ProtocolHelper.Protocols.ProFaceImport',

            'ByPlatform.Base.OutPutHelper',
            'ByPlatform.Base.StringHelper',
            'ByPlatform.Base.TimeHelper',
            'ByPlatform.Base.UtilHelper',
            'ByPlatform.Base.MonitorHelper.MonitorActivityHook',
            'ByPlatform.Base.MonitorHelper.MonitorHelper',
            'ByPlatform.Base.MonitorHelper.TimeKeeping',
            'ByPlatform.Base.NetHelper.NetHelper',
            'ByPlatform.Base.NetHelper.NetHelperEx',
            'ByPlatform.Base.NetHelper.UrlHelper',

            'ByPlatform.Base.FileAndDirect',
            'ByPlatform.DocumentHelper.ExcelHelper',
            'ByPlatform.DatebaseHelper.MysqlHelper',
            'ByPlatform.DatebaseHelper.MysqlConnectInfo',
],
)