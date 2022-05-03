# -*- coding: windows-1250 -*-
import redis


class Osztaly():
        
    def __init__(self):
        redis_host='172.22.203.190'
        redis_port=6379
               
        self.r=redis.Redis(host=redis_host, 
                           port=redis_port, 
                           decode_responses=True)
        
    def uj_dolg(self, email, nev):
        if self.r.hexists('felhasznalok', email):
            print('mar van ilyen email')
            return
        
        self.r.hset('felhasznalok', email, nev)
        
    def dolg_nev(self, email):
        print(self.r.hget('felhasznalok', email))
        
    def dolg_email(self, nev):
        for i in self.r.hkeys('felhasznalok'):
            if self.r.hget('felhasznalok', i)==nev:
                print(i)
                
    def dolg_lista(self):
        print(self.r.hgetall('felhasznalok'))
                
    def uj_feladat(self, kiiro_email, leiras, prioritas):
        if not(self.r.hexists('felhasznalok', kiiro_email)):
            print('nincs ilyen dolg')
            return
        
        f_azon=str(self.r.incr('f_azon'))
        
        
        self.r.hmset('feladat_'+f_azon,
                     {'kiiro_email':kiiro_email, 
                      'leiras':leiras})
        self.r.zadd('feladatok', f_azon, prioritas)
        return f_azon
        
    def feladat_lista(self):
        print(self.r.zrange('feladatok', 0, -1, 
                            withscores=True))
        
    def feladat_dolgozo_rendeles(self, email, f_azon):
        #if not(self.r.exists('feladat_'+f_azon)):
        if self.r.zscore('feladatok', f_azon)==None:
            print('nincs feladat')
            return
        
        if not(self.r.hexists('felhasznalok', email)):
            print('nincs ilyen dolg')
            return
        
        self.r.sadd('feladat_munkavegzes_'+f_azon, email)
        
    def lehetseges_munkavegzok_listaja(self, f_azon):
        for i in self.r.smembers('feladat_munkavegzes_'+f_azon):
            print(i)
            print(self.r.hget('felhasznalok', i))
            
    def feladat_leiras(self,f_azon):
        print(self.r.hget('feladat_'+f_azon, 'leiras'))
        
        print(self.r.hgetall('feladat_'+f_azon))
        print(self.r.zscore('feladatok', f_azon))
        
    def munka_elvegzes(self, f_azon, email):
        if not(self.r.sismember('feladat_munkavegzes_'+f_azon, 
                               email)):
            print('ezt a feladatot ezt a dolgozo nem vegezjeti')
            return
        
        self.r.zrem('feladatok', f_azon)
        self.r.delete('feladat_'+f_azon)
        self.r.delete('feladat_munkavegzes_'+f_azon)
        self.r.zincrby('elvegzett_feladatok', email, 1)
        
    def dolgozo_db_szerint(self):
        print(self.r.zrevrange('elvegzett_feladatok', 0 ,-1, 
                               withscores=True))
        
        for i in self.r.zrevrange('elvegzett_feladatok', 0 ,-1, 
                               withscores=False):
            print(i)
            print(self.r.hget('felhasznalok', i))
            print(self.r.zscore('elvegzett_feladatok', i))
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        