# -*- coding: windows-1250 -*-
import redis

class CFOsztaly():
        
    def __init__(self):
        redis_host='172.22.203.190'
        redis_port=6379
               
        self.r=redis.Redis(host=redis_host, port=redis_port, 
                           decode_responses=True)
        
    def uj_helyszin(self, nev):
        self.r.sadd('s_helyszinek', nev)
        
    def helyszin_lista(self):
        print(self.r.smembers('s_helyszinek'))
        
    def uj_esemeny(self, helyszin, kezdet, veg,megnevezes,
                   felelos_nev, felelos_tel):
        if not(self.r.sismember('s_helyszinek', helyszin)):
            print('Nincs ilyen helyszin')
            return
        if kezdet>=veg:
            print('Hibas idointervallum')
            return 
        
        for i in self.r.zrange('z_esemenyek', 0, -1
                               , withscores=False):
            if helyszin==self.r.hget(i, 'helyszin'):
                tk=self.r.hget(i,'esemeny_kezdete')
                tv=self.r.hget(i,'esemeny_vege')
                if ((kezdet<=tk and tk<=veg and veg<=tv)
                or (tk<=kezdet and kezdet<=tv and tv<=veg)
                or (kezdet<=tk and tv<=veg)
                or tk<=kezdet and veg<=tv):
                    print('Más van a szinpadon') 
                    return
        
        
        a=str(self.r.incr('esemeny_azon'))
        self.r.hmset('s_esemeny_'+a,
                     {'helyszin':helyszin, 
                      'esemeny_kezdete':kezdet, 
                      'esemeny_vege':veg,
                      'megnevezes':megnevezes,
                      'felelos_nev':felelos_nev, 
                      'felelos_tel': felelos_tel})
        self.r.zadd('z_esemenyek', 's_esemeny_'+a, kezdet)
        
    #5
    def esemeny_lista(self):
        for i in self.r.zrange('z_esemenyek',0,-1, 
                               withscores=False):
            print(i)
            print(self.r.hgetall(i))
            
    #4
    def esemeny_lista_idopontra(self, idopont):
        for i in self.r.zrange('z_esemenyek',0,-1, 
                               withscores=False):
            tk=self.r.hget(i,'esemeny_kezdete')
            tv=self.r.hget(i,'esemeny_vege')
            
            if (tk<=idopont and idopont<=tv):
                print(self.r.hgetall(i))
                
    def uj_jegytipus(self,nev, ar, erv_kezdet, erv_veg):
        self.r.sadd('s_jegytipusok', 'h_jegytipus_'+nev)
        self.r.hmset('h_jegytipus_'+nev, 
                     {'nev':nev, 
                      'ar':ar, 
                      'ervenyesseg_kezdete':erv_kezdet, 
                      'ervenyesseg_vege':erv_veg})
        
    def jegytipus_lista(self):
        for i in self.r.smembers('s_jegytipusok'):
            print(self.r.hgetall(i)) 
            
    def uj_vendeg(self,email, nev, szul_dat):
        self.r.sadd('s_vendegek', email)#
        self.r.hmset('h_vendeg_'+email, 
                     {'nev':nev, 
                      'email':email, 
                      'szul_dat':szul_dat})
        
    def vendeg_lista(self):
        for i in self.r.smembers('s_vendegek'):
            print(self.r.hgetall('h_vendeg_'+i))#   
            
    def vendeg_jegyet_vesz(self, email, jegytipus):
        if not(self.r.sismember('s_vendegek',email)):#
            print('nincs ilyen vendeg')
            return 
        if not(self.r.sismember('s_jegytipusok', 'h_jegytipus_'+jegytipus)):
            print('nincs ilyen jegytipus')
            return 
        
        self.r.sadd('s_'+email+'_jegyei',jegytipus)
        
    def vendeg_jegyeinek_listaja(self, email):
        print(self.r.smembers('s_'+email+'_jegyei'))  
        
    def vendeg_lista_idopontra(self,idopont):
        for i in self.r.smembers('s_vendegek'):
            for j in self.r.smembers('s_'+i+'_jegyei'):
                if (self.r.hget('h_jegytipus_'+j, 'ervenyesseg_kezdete')<=idopont
                    and idopont<=self.r.hget('h_jegytipus_'+j, 'ervenyesseg_vege')):
                    print(i) 
                    
    def like(self, email, esemeny):
        if not(self.r.sismember('s_vendegek', email)):
            print('nincs ilyen vendeg')
            return
            
        if not(self.r.exists(esemeny)):
            print('nincs ilyen esemeny')
            return
            
        if not(self.r.sismember('s_'+email+'_lajkok', esemeny)):
            self.r.sadd('s_'+email+'_lajkok', esemeny)
            self.r.zincrby('z_lajkok', esemeny, 1)
            
    def esemeny_lajkok(self):
        print(self.r.zrevrange('z_lajkok', 0, -1, withscores=True))
        
    def vendeg_lajkok(self, email):
        print(self.r.smembers('s_'+email+'_lajkok'))
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
    
    
    
    
    
    
    
    
    
    
          
    
        
         
    