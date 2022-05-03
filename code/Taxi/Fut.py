from TOszaly import TOsztaly
rf=TOsztaly()

rf.uj_auto('abc123', 'anna', '4', '2015', 'Opel', '123')
rf.uj_auto('abc124', 'geza', '3', '2016', 'Skoda', '222')
rf.uj_auto('abc124', 'geza', '3', '2016', 'Skoda', '222')
rf.uj_auto('ert345', 'elek', '4', '2014', 'VW', '111')

rf.auto_lista()

rf.auto_szolgalatba_all('abc123', '202204131000')
rf.auto_szolgalatba_all('abc124', '202204131200')
rf.auto_szolgalatba_all('ert345', '202204130900')

print('szolgalatlista')
rf.szolgalat_lista()

utid1=rf.ut_rendeles('Db Kassai 26', '202204131100', 4)
utid2=rf.ut_rendeles('Db Egyetem ter 1', '202204131110', 2)
utid3=rf.ut_rendeles('Db Interspar, Furedi u. 26', '202204131115', 1)
utid4=rf.ut_rendeles('Db Forum', '202204131120', 2)
utid5=rf.ut_rendeles('Db Piac u. 33', '202204131120', 2)

rf.ut_lista()

rf.auto_rendeles_uthoz(utid1, 'abc123')
rf.auto_rendeles_uthoz(utid2, 'abc123')
rf.auto_rendeles_uthoz(utid3, 'abc124')
rf.auto_rendeles_uthoz(utid4, 'abc124')

rf.ut_teljesites(utid1, 3000, 5)
rf.ut_teljesites(utid1, 5000, 8)
rf.ut_teljesites(utid2, 5000, 8)
rf.ut_teljesites(utid3, 2000, 3)

rf.megrendelt_lenemzart_utak()

print('osszkm')
rf.osszkm_lista()

rf.auto_adat('abc123')
print('osszar')
rf.osszar_lista()

rf.szolgalat_befejez('abc123', '202204132000')















