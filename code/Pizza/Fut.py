# -*- coding: windows-1250 -*-
from POsztaly import POsztaly

rf=POsztaly()

rf.uj_pizza('hawaii', 1300)
rf.uj_pizza('magyaros', 1500)
rf.uj_pizza('songoku', 1400)

rf.uj_feltet('hawaii', 'sajt')
rf.uj_feltet('hawaii', 'ananas')
rf.uj_feltet('hawaii', 'sonka')
rf.uj_feltet('hawaii', 'paradicsomszosz')

rf.uj_feltet('magyaros', 'kolbasz')
rf.uj_feltet('magyaros', 'szalonna')
rf.uj_feltet('magyaros', 'hagyma')
rf.uj_feltet('magyaros', 'paprika')

rf.uj_feltet('songoku', 'sonka')
rf.uj_feltet('songoku', 'gomba')
rf.uj_feltet('songoku', 'kukorica')
rf.uj_feltet('songoku', 'paradicsom')

rf.pizza_lista()

mra1=rf.megrendeles('Db Kassai 26', '202204061410')
print(mra1)
rf.megrendeles_pizza(mra1, 'hawaii', 3)
rf.megrendeles_pizza(mra1, 'magyaros', 4)

mra2=rf.megrendeles('Db laktanya 20', '202204061410')
print(mra2)
rf.megrendeles_pizza(mra2, 'songoku', 2)
rf.megrendeles_pizza(mra2, 'magyaros', 1)

rf.sutnivalo_pizza()

rf.sutni_kezd('1')
rf.sutni_kezd('2')
rf.sutni_kezd('3')
rf.sutni_kezd('4')

rf.sutoben_lista()
print('hello')
rf.sutnivalo_pizza()

rf.kesz('1')
rf.kesz('2')
rf.kesz('3')
rf.kesz('4')

rf.sutni_kezd('5')
rf.sutni_kezd('6')
rf.sutni_kezd('7')
rf.sutni_kezd('8')

rf.kesz('6')
rf.kesz('7')
rf.kesz('8')
rf.kesz('5')
print('almafa')
rf.sutoben_lista()
print('kortefa')
rf.kiszallit('1')
















