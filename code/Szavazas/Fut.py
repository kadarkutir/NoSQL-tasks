from Osztaly import Osztaly
rf=Osztaly()

rf.uj_cikk('macska', 'm.hu', 'anna', '20220501')
rf.uj_cikk('kutya', 'm.hu', 'anna', '20220501')
rf.uj_cikk('kutya', 'k.hu', 'bela', '20220428')
rf.uj_cikk('delfin', 'd.hu', 'anna', '20220427')
rf.uj_cikk('elefant', 'e.hu', 'cili', '20220501')

rf.cikk_lista()

rf.cikk_adatok('k.hu')

rf.szavazas('elek', 'e.hu')
rf.szavazas('elek', 'e.hu')
rf.szavazas('fanni', 'd.hu')
rf.szavazas('fanni', 'e.hu')
rf.szavazas('fanni', 'm.hu')
rf.szavazas('gabor', 'm.hu')
rf.szavazas('gabor', 'd.hu')
rf.szavazas('dani', 'd.hu')

rf.legtobb_szavazat()
rf.utolso_cikk()

rf.cikk_lista_by_szavazat()
