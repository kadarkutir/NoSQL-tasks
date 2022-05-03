# -*- coding: windows-1250 -*-
import redis
from time import sleep
from _datetime import datetime
from datetime import timedelta

class DOsztaly():
        
    def __init__(self):
        redis_host='172.22.203.190'
        redis_port=6379
               
        self.r=redis.Redis(host=redis_host, port=redis_port, 
                           decode_responses=True)
    def demon(self):
        while(True):
            sleep(10)#second
            v_time=(datetime.now()-timedelta(minutes=1)).strftime("%Y%m%d%H%M%S")
            
            for i in self.r.zrangebyscore('token_aktiv', 0, v_time, 
                                          withscores=False):
                self.r.hdel('tokenek', i)
                self.r.zrem('token_aktiv', i)
                
                
        