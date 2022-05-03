# -*- coding: windows-1250 -*-
import redis


class POsztaly():
        
    def __init__(self):
        redis_host='172.22.203.190'
        redis_port=6379
               
        self.r=redis.Redis(host=redis_host, 
                           port=redis_port, 
                           decode_responses=True)
        
    #1, 3        
    def uj_pizza(self, nev, ar):
        self.r.hset('pizzak', nev, ar)
        
    def uj_feltet(self, pizza, feltet):
        if not(self.r.hexists('pizzak', pizza)):
            print('nincs ilyen pizza')
            return 
        self.r.sadd('feltet_'+pizza, feltet)
        
    def pizza_lista(self):
        for i in self.r.hkeys('pizzak'):
            print(i)
            print(self.r.hget('pizzak', i))
            print(self.r.smembers('feltet_'+i))
            
    def megrendeles(self, cim, ido):
        mra=str(self.r.incr('mra'))
        self.r.hmset('mr_'+mra, 
                     {'cim':cim,
                      'ido':ido})
        self.r.sadd('megrendelesek', mra)
        return mra
        
        
    def megrendeles_pizza(self, mra, pizza, db):
        if not(self.r.sismember('megrendelesek', mra)):
            print('nincs ilyen megrendeles')
            return
        
        if not(self.r.hexists('pizzak', pizza)):
            print('nincs ilyen pizza')
            return 
        
        for i in range(db):
        
            mrr=str(self.r.incr('mrr'))
            self.r.hmset('mrr'+mrr, 
                         {'megrendeles_azon':mra,
                          'pizza':pizza})
            self.r.sadd('mrreszlet_'+mra, mrr)
            self.r.rpush('sutnivalo', mrr)
            
             
    def sutnivalo_pizza(self):
        for i in self.r.lrange('sutnivalo', 0 ,-1):
            print('mrr'+i)
            print(self.r.hget('mrr'+i, 'megrendeles_azon'))
            pizza=self.r.hget('mrr'+i, 'pizza')
            print(pizza)
            print(self.r.smembers('feltet_'+pizza))
            
    def sutni_kezd(self, mrr):
        
        if self.r.lrem('sutnivalo', mrr, 1)==0:
            print('nincs ilyen reszlet')
            return
        self.r.rpush('sutobe', mrr)
        
    def sutoben_lista(self):
        print(self.r.lrange('sutobe', 0, -1))
        
    def kesz(self, mrr):
        if self.r.lrem('sutobe', mrr, 1)==0:
            print('nincs ilyen reszlet')
            return 
        self.r.rpush('kesz_pizzak', mrr)
        
        mra=self.r.hget('mrr'+str(mrr), 'megrendeles_azon')
        print('kesz:'+mra)
        
        kesz=True
        for i in self.r.lrange('sutnivalo', 0,-1):
            if mra==self.r.hget('mrr'+i, 'megrendeles_azon'):
                kesz=False
                
        for i in self.r.lrange('sutobe', 0,-1):
            if mra==self.r.hget('mrr'+i, 'megrendeles_azon'):
                kesz=False
        print(kesz)
        if kesz:
            self.r.rpush('kesz_megrendeles', mra)
            for i in self.r.smembers('mrreszlet_'+mra):
                self.r.lrem('kesz_pizzak', i)
                
    def kiszallit(self, mra):
        if self.r.lrem('kesz_megrendeles', mra)==0:
            print('nincs ilyen megrendeles')
            return
        
        for i in self.r.smembers('mrreszlet_'+str(mra)):
            self.r.delete(i)
        self.r.delete('mrreszlet_'+i)
        self.r.delete('mr_'+mra)
            
            
            
            
            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
            
            
            
            
            
            
            
            
            
            
            
