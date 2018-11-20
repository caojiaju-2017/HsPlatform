# -*- coding: utf-8 -*- # 
# by oldj http://oldj.net/ #  
import pythoncom,time,datetime,os
import pyHook

LastRecordTime = None
currentKey = "control"
def haveAction(type = 0):
    global LastRecordTime

    # 获取当前时间
    currentTime = datetime.datetime.now()

    # 计算当前时间何 配置时间 差
    start = datetime.datetime.strptime(LastRecordTime, "%Y-%m-%d %H:%M:%S")

    timeGo = (currentTime - start).seconds
    # print u"Time lost :%d 秒"%timeGo
    count = 1.5*60
    # count = 1
    if timeGo >= count*60 and "control" not in currentKey:
        shutdownComputer()
        print "shutdown command"
    # elif  timeGo < count*60:
    #     print "not timeout"
    # else:
    #     print "have press control"
    pass

def shutdownComputer():
    print 'i want shutdown computer'
    cmd = 'shutdown -s -t 1'
    try:
        os.system(cmd)
    except Exception , ex:
        pass
    pass

def onMouseEvent(event):
    haveAction(0)
    # 监听鼠标事件     
    # print  "MessageName:", event.MessageName
    # print "Message:", event.Message
    # print "Time:", event.Time
    # print "Window:", event.Window
    # print "WindowName:", event.WindowName
    # print "Position:", event.Position
    # print "Wheel:", event.Wheel
    # print "Injected:", event.Injected
    # print"---"

    # 返回 True 以便将事件传给其它处理程序
    # 注意，这儿如果返回 False ，则鼠标事件将被全部拦截
    # 也就是说你的鼠标看起来会僵在那儿，似乎失去响应了
    return True

def onKeyboardEvent(event):
    global currentKey
    haveAction(1)
    # 监听键盘事件
    # print "MessageName:", event.MessageName
    # print "Message:", event.Message
    # print "Time:", event.Time
    # print "Window:", event.Window
    # print "WindowName:", event.WindowName
    # print "Ascii:", event.Ascii, chr(event.Ascii)
    # print "Key:", event.Key
    currentKey = event.Key
    # print "KeyID:", event.KeyID
    # print "ScanCode:", event.ScanCode
    # print "Extended:", event.Extended
    # print "Injected:", event.Injected
    # print "Alt", event.Alt
    # print "Transition", event.Transition
    # print "---"
    # 同鼠标事件监听函数的返回值     
    return True


def readConfig():
    global  LastRecordTime
    # 读取文件
    f = open('last.txt')
    context = f.read()
    f.close()

    configDateTime = context.strip()

    # 获取当前日期
    currentTime = time.strftime("%Y-%m-%d", time.gmtime())

    # 判断当前日期是否为配置文件日期
    if not configDateTime or configDateTime[:10] < currentTime:
        currentTime = datetime.datetime.now()

        LastRecordTime = currentTime.strftime("%Y-%m-%d %H:%M:%S") # time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
        updateConfig(LastRecordTime)
    else:
        LastRecordTime = configDateTime

    pass

def updateConfig(newtime):
    f1 = open('last.txt', 'w')
    f1.write(newtime)
    f1.close()
    pass

def main():
    # 读取配置文件
    readConfig()

    # 创建一个“钩子”管理对象     
    hm = pyHook.HookManager()
    # 监听所有键盘事件     
    hm.KeyDown = onKeyboardEvent
    # 设置键盘“钩子”     
    hm.HookKeyboard()
    # 监听所有鼠标事件     
    hm.MouseAll = onMouseEvent
    # 设置鼠标“钩子”     
    hm.HookMouse()
    # 进入循环，如不手动关闭，程序将一直处于监听状态     
    pythoncom.PumpMessages()

def testFunction():
    pass
if __name__ == "__main__":
    main()