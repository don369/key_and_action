#-*- coding:utf-8 -*-
import openbrowser
import onKeyLog

b = openbrowser.OpenBrowser()

Logs = openbrowser.klog

for log in Logs.selectAll().fetchall():
    print(u"按键 %s , 已按下 %s 次" % (log[1], log[2]))

b.action("1", "http://www.163.com")
b.action("2","http://www.baidu.com")
b.run()
