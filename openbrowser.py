#-*- coding:utf-8 -*-
import os
from Tkinter import *
import subprocess
import webbrowser
import platform
import onKeyLog


klog = onKeyLog.OnKeyLog()

class OpenBrowser(object):

    def __init__(self, geometry="60*60"):
        self.key_event_hash = {}
        self.win = Tk()
        self.win.geometry('60x60')

    def action(self, key, url):
        self.key_event_hash[key] = { "method": "browser", "action": url }
        return self

    def openFinder(self, key, url):
        self.key_event_hash[key] = { "method": "finder", "action": url }
        return self

    def run(self):
        self._stick()
        self.win.bind('<Key>', self._keyEvent)
        self.win.mainloop()

    def close(self):
        self.win.quit()
        klog.close()

    def _keyEvent(self, event):
        key = self.key_event_hash[event.char]
        print("当前按下的按键： %s" % event.char)
        if key == None:
            return False

        method = key["method"]
        action = key["action"]
        
        if method == "browser":
            webbrowser.open(action)
        elif method == "finder":
            c = subprocess.Popen(["/usr/bin/open", action])
            c.wait()
        klog.onKeyCount(event.char)

        self.close()

    def _stick(self):
        sys = platform.system()
        if sys == "Windows":
            self.win.attributes("-topmost", 0)
        elif sys == "Darwin":
            tmpl = 'tell application "System Events" to set frontmost of every process whose unix id is {} to true'
            script = tmpl.format(os.getpid())
            subprocess.check_call(['/usr/bin/osascript', '-e', script])
            pass

