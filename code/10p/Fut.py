from Osztaly import Osztaly
rf=Osztaly()

rf.uj_dolg('a@g.c', 'anna')
rf.uj_dolg('a@g.c', 'anna2')
rf.uj_dolg('b@g.c', 'bela')
rf.uj_dolg('c@g.c', 'cili')
rf.uj_dolg('d@g.c', 'denes')
rf.uj_dolg('e@g.c', 'elek')
rf.uj_dolg('f@g.c', 'elek')

rf.dolg_email('elek')
rf.dolg_nev('a@g.c')
rf.dolg_lista()

rf.uj_feladat('w@g.c', 'ablakpucolas', 2)
f1=rf.uj_feladat('a@g.c', 'ablakpucolas', 2)
f2=rf.uj_feladat('a@g.c', 'felmosas', 3)
f3=rf.uj_feladat('a@g.c', 'mosogatas', 5)

rf.feladat_lista()

rf.feladat_dolgozo_rendeles('b@g.c', f1)
rf.feladat_dolgozo_rendeles('c@g.c', f1)

rf.feladat_dolgozo_rendeles('c@g.c', f2)
rf.feladat_dolgozo_rendeles('d@g.c', f2)
rf.feladat_dolgozo_rendeles('e@g.c', f2)

rf.feladat_dolgozo_rendeles('d@g.c', f3)

rf.feladat_dolgozo_rendeles('d@g.c', '-1')
rf.feladat_dolgozo_rendeles('w@g.c',f3)


rf.lehetseges_munkavegzok_listaja(f2)

print('***')

rf.feladat_leiras(f3)
rf.feladat_leiras('-1')


rf.munka_elvegzes(f3, 'd@g.c')
rf.munka_elvegzes(f3, 'a@g.c')
rf.munka_elvegzes(f2, 'w@g.c')

rf.munka_elvegzes(f2, 'd@g.c')
rf.munka_elvegzes(f1, 'b@g.c')

print('*-*')
rf.dolgozo_db_szerint()














