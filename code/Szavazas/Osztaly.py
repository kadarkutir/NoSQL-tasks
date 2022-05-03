# -*- coding: windows-1250 -*-
import redis
from _datetime import datetime

class Osztaly():
        
    def __init__(self):
        redis_host='172.22.203.190'
        redis_port=6379
               
        self.r=redis.Redis(host=redis_host, port=redis_port, 
                           decode_responses=True)

    def uj_cikk(self, cim, link, posztolo, datum):
        self.r.hmset('cikk_'+link,
                     {'cim':cim, 
                      'link':link, 
                      'posztolo':posztolo, 
                      'datum':datum})
        self.r.zadd('cikkek_datum', link, datum)
        
    def cikk_adatok(self, link):
        print(self.r.hgetall('cikk_'+link))
        
    def cikk_lista(self):
        for i in self.r.zrevrange('cikkek_datum', 0, -1, withscores=True):
            print(i)
            #print(self.r.hgetall('cikk_'+i)
            
    def szavazas(self, felh, link):
        if self.r.zscore('cikkek_datum', link)==None:
            print('nincs cikk')
            return
        
        if not(self.r.sismember(felh+'_szavazat', link)):
            self.r.sadd(felh+'_szavazat', link)
            self.r.zincrby('szavazatok', link, 1)
            
    def cikk_lista_by_szavazat(self):
        print(self.r.zrevrange('szavazatok', 0, -1, withscores=True))
              
    def legtobb_szavazat(self):
        print(self.r.zrevrange('szavazatok', 0, 0, withscores=True))
        
    def utolso_cikk(self):
        print(self.r.zrevrange('cikkek_datum', 0, 0, withscores=False))
        
        
        for c in self.r.zrevrange('cikkek_datum', 0, 0, withscores=False):
            sc=self.r.zscore('cikkek_datum', c)
            
            print(self.r.zrevrangebyscore('cikkek_datum', sc, sc))
        
        