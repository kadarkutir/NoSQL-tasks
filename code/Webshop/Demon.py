# -*- coding: windows-1250 -*-
import redis
from time import sleep
from _datetime import datetime
from datetime import timedelta

redis_host='172.22.203.190'
redis_port=6379
               
r=redis.Redis(host=redis_host, port=redis_port, 
                           decode_responses=True)

        
while(True):
    sleep(10)#second
    v_time=(datetime.now()-timedelta(minutes=1)).strftime("%Y%m%d%H%M%S")
            
    for i in r.zrangebyscore('aktivitas', 0, v_time, 
                                          withscores=False):
        r.hdel('tokenek', i)
        r.zrem('aktivitas', i)
        
    print(r.rpop('megrendelve'))