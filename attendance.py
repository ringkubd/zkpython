# -*- coding: utf-8 -*-
import sys
import json
import time
import asyncio

sys.path.append("zk")

from zk import ZK, const

class Attendance:
    'All attendance report'
    conn = None
    zk = ""
    attendancelogv = ()

    def __init__(self, deviceIp):
        super().__init__()
        self.connection(deviceIp)
        
        
    def connection(self, deviceIp, dport = 4370, timeout = 5, password=0, force_udp = False, ommit_ping = False):
        self.zk = ZK(deviceIp, dport, timeout, password, force_udp, ommit_ping)
        try:
            self.conn = self.zk.connect()
        except Exception as e:
            return json.dumps({"status": "error", "message": e.args});
        
        return self.conn;
    
    async def attLog(self):
        self.attendancelogv =  self.conn.get_attendance();


    async def attendanceLog(self):
        #await asyncio.sleep(5)
        await self.attLog();
        data = []
        for attn in self.attendancelogv:
            data.append(attn.jsonreturn())
            
        
        # print(data)
        jsonData = json.dumps(data)
        print(jsonData)
        
    def switcher(self, argument):
        print(argument);
        switcher = {
            'attendance' : asyncio.run(self.attendanceLog()),
            'a' : 123
        }
        return switcher.get(argument, 'Method not found')


Attendance(sys.argv[1]).switcher(sys.argv[2])
