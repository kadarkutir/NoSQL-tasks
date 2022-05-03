# -*- coding: windows-1250 -*-
from CFOsztaly import CFOsztaly

rf=CFOsztaly()

rf.uj_helyszin('DEIK szinpad')
rf.uj_helyszin('Stadion szinpad')
rf.uj_helyszin('OTP szinpad')
rf.uj_helyszin('Egoist szinpad')

rf.helyszin_lista()

# rf.uj_esemeny('DEIK szinpad', '202203161000', '202203161100', 
#               'Tankcsapda', 'Geza', '123')
# rf.uj_esemeny('DEIK szinpad', '202203161000', '202203160900', 
#               'Tankcsapda', 'Geza', '123')
# rf.uj_esemeny('DEIK szinpad', '202203161030', '202203161050', 
#               'Shakira', 'Gabor', '124')
# rf.uj_esemeny('DEIK szinpad', '202203161110', '202203161230', 
#               'Shakira', 'Gabor', '124')
#
# rf.uj_esemeny('Egoist szinpad', '202203161100', '20220316120', 
#               'Republik', 'Dani', '125')

rf.esemeny_lista()

print()

#rf.esemeny_lista_idopontra('202203161112')
#
# rf.uj_jegytipus('felnott_heti', 20000, '202203140000', '202203220000')
# rf.uj_jegytipus('felnott_hetfo', 5000, '202203140000', '202203150000')
# rf.uj_jegytipus('felnott_kedd', 5000, '202203150000', '202203160000')
# rf.uj_jegytipus('gyerek_kedd', 2000, '202203150000', '202203160000')

rf.jegytipus_lista()
#
# rf.uj_vendeg('g@g.c', 'Gabor', '20000101')
# rf.uj_vendeg('a@g.c', 'Anna', '20000102')
# rf.uj_vendeg('david@g.c', 'David', '20000102')
# rf.uj_vendeg('marci@g.c', 'Marci', '20000103')

rf.vendeg_lista()

# rf.vendeg_jegyet_vesz('b@g.c', 'gyerek_szerda')
# rf.vendeg_jegyet_vesz('a@g.c', 'gyerek_szerda')
# rf.vendeg_jegyet_vesz('a@g.c', 'gyerek_kedd')
# rf.vendeg_jegyet_vesz('marci@g.c', 'felnott_kedd')
# rf.vendeg_jegyet_vesz('marci@g.c', 'felnott_hetfo')
# rf.vendeg_jegyet_vesz('david@g.c', 'felnott_heti')
# rf.vendeg_jegyet_vesz('g@g.c', 'felnott_kedd')
# rf.vendeg_jegyet_vesz('g@g.c', 'felnott_hetfo')

#rf.vendeg_jegyeinek_listaja('g@g.c')

rf.vendeg_lista_idopontra('202203141000')

rf.like('a@g.c', 's_esemeny_2')
rf.like('a@g.c', 's_esemeny_1')
rf.like('x@g.c', 's_esemeny_x')
rf.like('a@g.c', 's_esemeny_x')
rf.like('x@g.c', 's_esemeny_1')
rf.like('g@g.c', 's_esemeny_1')
rf.like('a@g.c', 's_esemeny_1')
rf.like('g@g.c', 's_esemeny_3')
rf.like('marci@g.c', 's_esemeny_1')

rf.esemeny_lajkok()

rf.vendeg_lajkok('a@g.c')

