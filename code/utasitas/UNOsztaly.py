# -*- coding: windows-1250 -*-
import redis
import uuid
from _datetime import datetime

class UNOsztaly():
        
    def __init__(self):
        redis_host='172.22.203.190'
        redis_port=6379
               
        self.r=redis.Redis(host=redis_host, port=redis_port, 
                           decode_responses=True)
        
    def uj_felh(self, nev, jelszo):
        if self.r.hexists('felhasznalok', nev):
            print('foglalt nev')
            return 
        self.r.hset('felhasznalok', nev, jelszo)
        
    def felh_lista(self):
        #print(self.r.hkeys('felhasznalok'))
        print(self.r.hgetall('felhasznalok'))
        
    def elfelejtett_jelszo(self, nev):
        print(self.r.hget('felhasznalok', nev))
        
    def generate_token(self):
        return str(uuid.uuid4())
    
    def bejelentkezik(self, nev, jelszo):
        if jelszo!=self.r.hget('felhasznalok', nev):
            print('hibas jelszo')
            return
        tok=self.generate_token()
        self.r.hset('tokenek', tok, nev)
        ido=datetime.now().strftime("%Y%m%d%H%M%S")  
        self.r.zadd('token_aktiv', tok, ido)
        return tok
        
    def token_lista(self):
        print(self.r.hkeys('tokenek'))
        
    def erv_tok(self, tok):
        return self.r.hexists('tokenek', tok)
    
    def utasitas(self, tok, ut):
        felh=self.r.hget('tokenek', tok)
        if felh!=None:
            self.r.lpush('ut_'+felh, ut)
            self.r.ltrim('ut_'+felh, 0,4)
            
            ido=datetime.now().strftime("%Y%m%d%H%M%S")  
            self.r.zadd('token_aktiv', tok, ido)
            
    def ut_lista(self, tok):
        felh=self.r.hget('tokenek', tok)
        if felh!=None:
            print(self.r.lrange('ut_'+felh, 0, -1))
            
            ido=datetime.now().strftime("%Y%m%d%H%M%S")  
            self.r.zadd('token_aktiv', tok, ido)
            
    def kijelentkezik(self, tok):
        self.r.hdel('tokenek', tok)









