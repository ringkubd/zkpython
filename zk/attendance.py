# -*- coding: utf-8 -*-
import json;

class Attendance(object):
    def __init__(self, user_id, timestamp, status, punch=0, uid=0):
        self.uid = uid # not really used any more
        self.user_id = user_id
        self.timestamp = timestamp
        self.status = status
        self.punch = punch

    def __str__(self):
        #return '<Attendance>: {} : {} ({}, {})'.format(self.user_id, self.timestamp, self.status, self.punch)
        return '<Attendance> uid:{} ,punch_time:{}, status: {}, punch:{}'.format(self.user_id, self.timestamp, self.status, self.punch)

    def __repr__(self):
        #return '<Attendance>: {} : {} ({}, {})'.format(self.user_id, self.timestamp,self.status, self.punch)
        return '<Attendance> uid:{} ,punch_time:{}, status: {}, punch:{}'.format(self.user_id, self.timestamp,self.status, self.punch)    

    def jsonreturn(self):
        return json.dumps({'user_id': self.user_id, 'timestamp': self.timestamp.strftime("%m-%d-%Y, %H:%M:%S"), 'status': self.status, 'punch': self.punch});
