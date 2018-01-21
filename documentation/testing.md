# Testausdokumentti

Testauksessa testataan seuraavia asioita:

Mukien tunnistaminen:
Mukien tunnistamiseen pääasiassa käytetään oikeaa koodia mutta ilman drone.takeoff() -komentoa. Tällöin drone käyttää omaa pohjakameraansa ja akku kestää hyvin pitkään, aikaan saadaan realistinen testi. Alkuvaiheessa testasin mukien tunnistamista myös kannettavan webcamin kautta, mutta se ei anna yhtä realistista kuvaa sillä dronen kamera on huomattavasti epätarkempi.

Mukin päällä hoveroiminen:
Mukien päällä hoveroimisen toimivuus testataan käytännössä: käynnistetään drone ja asetetaan sen alle muki. Jos drone karkaa omille teilleen, se kaapataan manuaaliohjauksella ja siirretään takaisin omalle paikalleen.

Mukiin osuminen pongipallolla:
Osumistarkkuus ja hienosäätö (missä kohtaa mukin tulee olla jotta osumistarkkuus on paras) tehdään käytännön testauksilla ja toistoilla.

Muu testaus:
Koodi ei varsinaisesti sisällä muuta testattavaa. Kontrollien toimivuus yms testataan yhdellä koeajolla.
