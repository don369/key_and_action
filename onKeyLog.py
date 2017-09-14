#-*- coding:utf-8 -*-
import sqlite3
import os

class OnKeyLog(object):
    def __init__(self):
        path = os.path.join(os.getcwd(), "keylog.db")
        has_DB_file = os.path.exists(path)
        self._conn = sqlite3.connect(path)
        self.c = self._conn.cursor()
        if not has_DB_file:
            self.c.execute('''CREATE TABLE keylog (
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                key text, 
                count INTEGER)''')
            self._conn.commit()
    
    def add(self, Key):
        self.c.execute("insert into keylog(key,count) values ( %s , 1)" % Key)
        self._conn.commit()

    def update(self, Key, count):
        self.c.execute("update keylog set count= %i where Key= '%s'" % (count, Key))
        self._conn.commit()

    def selectCount(self, Key):
        rs = self.c.execute("select count from keylog where Key='%s'" % Key)
        rs = rs.fetchone() 
        return rs[0] if rs != None else False

    def onKeyCount(self, Key):
        count = self.selectCount(Key) + 1
        self.update(Key, count) if count else self.add(Key)

    def delete(self, Key):
        self.c.execute("DELETE from keylog where key = %s" % Key)
        self._conn.commit()

    def selectAll(self):
        return self.c.execute("select * from keylog")

    def close(self):
        self._conn.close()


