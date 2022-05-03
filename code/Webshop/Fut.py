# -*- coding: windows-1250 -*-
from Osztaly import Osztaly

rf=Osztaly()

# rf.uj_felh('anna', 'ja', 'a@g.c', 'Anna K', 2001)
# rf.uj_felh('anna', 'ja', 'a@g.c', 'Anna K', 2002)
# rf.uj_felh('bela', 'jb', 'b@g.c', 'Bela B', 2001)
# rf.uj_felh('cili', 'jc', 'c@g.c', 'Cili Cs', 2000)
# rf.uj_felh('denes', 'jd', 'd@g.c', 'Denes Cs', 2000)
# rf.uj_felh('endre', 'je', 'e@g.c', 'E E', 2002)

# rf.felhasznalo_lista()

# rf.torol_felh_email('e@g.c')
# rf.torol_felh_nev('denes')
print()
rf.felhasznalo_lista()
# rf.elfelejtett_jelszo('anna')

tok_a=rf.bejelentkezik('anna', 'ja')
tok_a2=rf.bejelentkezik('anna', 'ja')
# print(tok_a)
# print(rf.bejelentkezik('anna', 'ra'))
# print(rf.bejelentkezik('endre', 'ra'))
tok_b=rf.bejelentkezik('bela', 'jb')
# print(tok_b)
#
# print(rf.erv_tok(tok_a))

rf.token_lista()

# rf.uj_cikk('alma')
# rf.uj_cikk('kenyer')
# rf.uj_cikk('dio')
# rf.uj_cikk('tv')
# rf.uj_cikk('olomkatona')

rf.cikk_lista()

rf.kosarba_tesz(tok_a, 'alma', 2)
rf.kosarba_tesz(tok_a, 'kenyer', 3)
rf.kosarba_tesz(tok_a2, 'dio', 10)
rf.kosarba_tesz(tok_b, 'olomkatona', 10)

rf.kosar_lista(tok_a)

rf.kosar_lista(tok_b)

rf.megrendeles(tok_a, 'Db', '123')
rf.megrendeles(tok_b, 'Bp', '124')

rf.megrendeles_lista()