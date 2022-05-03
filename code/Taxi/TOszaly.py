# -*- coding: windows-1250 -*-
import redis


class TOsztaly():
        
    def __init__(self):
        redis_host='172.22.203.190'
        redis_port=6379
               
        self.r=redis.Redis(host=redis_host, port=redis_port, 
                           decode_responses=True)
        
    def uj_auto(self, rendszam, sofor, utas_db,
                auto_evj, autotipus, tel):
        if self.r.sismember('autok', rendszam):
            print('mar van ilyen rendszam')
            return

        self.r.hmset('auto_'+rendszam,
                     {'rendszam':rendszam, 
                      'sofor':sofor, 
                      'utas_db':utas_db,
                      'auto_evj':auto_evj, 
                      'autotipus':autotipus, 
                      'tel':tel})
        self.r.sadd('autok', rendszam)

    def auto_lista(self):
        for i in self.r.smembers('autok'):
            print(self.r.hgetall('auto_'+i))
            
    def auto_szolgalatba_all(self, rendszam, idopont):
        if not(self.r.sismember('autok', rendszam)):
            print('nincs ilyen rendszam')
            return
        
        self.r.zadd('szolgalat', rendszam, idopont)
        
    def szolgalat_befejez(self, rendszam, idopont):
        #idopont vizsgalat
        
        self.r.zrem('szolgalat', rendszam)
        self.r.zrem('osszar', rendszam)
        
    def szolgalat_lista(self):
        print(self.r.zrevrange('szolgalat', 0, -1, 
                               withscores=True))
        
    def ut_rendeles(self, cim, idopont, letszam):
        if letszam>4:
            print('sokan vannak')
            return
        
        utid=str(self.r.incr('utid'))
        self.r.hmset('ut_'+utid, 
                     {'cim':cim,
                      'idopont':idopont,
                      'letszam':letszam})
        self.r.sadd('utak', utid)
        return utid
        
    def auto_rendeles_uthoz(self, utid, rendszam):
        if not(self.r.sismember('utak', utid)):
            print('nincs ilyen ut')
            return
        if not(self.r.sismember('autok', rendszam)):
            print('nincs ilyen rendszam')
            return
        
        self.r.hset('ut_'+utid, 'rendszam', rendszam)
        
    def ut_teljesites(self, utid, ar, km):
        
        rendszam=self.r.hget('ut_'+utid, 'rendszam')
        
        if rendszam==None:
            print('nincs auto')
            return 
        
        if self.r.hexists('ut_'+utid, 'ar'):
            print('teljesitve')
            return
        
        self.r.hmset('ut_'+utid, {'ar':ar, 'km':km})
        self.r.zincrby('osszkm', rendszam, km)
        self.r.zincrby('osszar', rendszam, ar)
        
    def osszkm_lista(self):
        for i in self.r.zrange('osszkm', 0, -1, 
                               withscores=False):
            print(i)
            print(self.r.zscore('osszkm', i))
            print(self.r.hget('auto_'+i, 'sofor'))
            
    def auto_adat(self, rendszam):
        print(self.r.hgetall('auto_'+rendszam))
        
    def ut_lista(self):
        print('utlista')
        for i in self.r.smembers('utak'):
            print(i)
            print(self.r.hgetall('ut_'+i))
            
    def megrendelt_lenemzart_utak(self):
        print('lenemzart_utak')
        for i in self.r.smembers('utak'):
            if not(self.r.hexists('ut_'+i, 'ar')):
                print(i)
                print(self.r.hgetall('ut_'+i))
                
    def osszar_lista(self):
        print(self.r.zrange('osszar', 0, -1, withscores=True))
        
        
        
        
        
        
        
        
        
        
        
        
        
        
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
        
        
        
        
        
        
        
        
        










        
   