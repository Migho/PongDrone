# Viikkoraportit

## Viikkoraportti 1 (23.12)

Tällä viikolla olen tutkinut miten drone toimii ja miettinyt aihettani. So far ongelmia ei ole ollut, mutta pöhistessä niitä nyt ei vielä kuulukaan tulla. Dronen mukana tulleista akuista vain toinen toimii ja dronen kuori itsessään sisältää melkoisesti teippauksia. Lisäksi yksi siipi on vääntynyt, muttei haittaa lentämistä. Drone ilmeisesti on melko hyvä kalibroimaan itsensä ja pysymään tasapainossa huonommasta siivestä ja epätasapainoisesta kuoresta huolimatta.

Dronen rajapinta vaikuttaa hyvältä ja varsin laajalta. Ainut huono puoli että USB-säätöjä on ilmeisesti vain yksi: dronen voi asettaa tallentamaan videokuvaa USB-tikulle. Aion vielä selvittää onko USB-paikkaa mahdollista hyödyntää tässä projektissa mutta ainakin toistaiseksi elän siinä uskossa ettei se ole mahdollista.

Seuraavaksi selvitän käytännön kokeiluilla voiko USB-paikkaa hyödyntää ja teen testejä onko palloa mahdollista pudottaa jonkinlaisella rautalankasysteemillä (kts määrittelydokumentti). 

Käytetyt tunnit: 5h

Btw ohjaajat, olen muuten välipäivät landella enkä uskaltanut dronea kuljettaa 400 kilometriä. Konkreettista koodia voi tämän vuoksi olla ensi viikolla kovin vähän tai ei ollenkaan, onko se ok? Olen valmis tekemään dokumentaatiota sen sijaan (selvitystä miten toteutan mukien tunnistuksen).

## Viikkoraportti 2 (29.12)

Tähän deadlinen varsinaiseen päivään ei minulla varsinaisesti ole mitään kunnollista näytettävää - olen maanantaihin asti landella ilman dronea. Jules lupasi että palautuspäivää voidaan osaltani lykätä tiistaille.

Käytetyt tunnit: 2h

## Viikkoraportti 2.1 (2.1)

Sain dronen taas käyttööni ja tutkin useampia erilaisia kirjastoja Dronen ohjaamiseen. Loppupeleissä kokonaan oman kirjaston tekeminen ei olisi ollut mahdoton tehtävä mutta olisi kuitenkin syönyt ominaisuuksia lopulliselta sovellukselta joten päätin käyttää valmista kirjastoa. Valmistajan oma SDK olisi ollut C-kielellä jota en osaa. Varsin moni kirjastoista oli hyvä käyttää mutta PS-Drone oli mielestäni parhaiten kehitetty ja omasi parhaan dokumentaation: http://www.playsheep.de/drone

Vasta tällä viikolla havaitsin että dronessa on myös pohjakamera (!), jonka sain kirjastolla onnistuneesti käyttööni. Omaa koodia ei itse repossa ole vielä ollenkaan, mutta sain dronen tekemään kaiken mitä halusinkin esimerkkikoodeilla ja omilla koodeillani. Havaitsin myös että dronella on mahdollista tehdä pyörähdyksiä ja muita temppuja. USB-porttia yritin saada toimimaan mutta sitä ei ole mahdollista tässä hyödyntää.

Torstaiksi yritän saada aikaiseksi oikeaa koodia esimerkiksi punaisen värin tunnistamista ja seuraamista (?) varten.

Käytetyt tunnit: 4h

## Viikkoraportti 3 (5.1)

Tältä puolelta viikolta kului hyvin paljon aikaa pelkästään kuvantunnistuksen opetteluun. Alusta asti oli jo melko selvää että valinta on cv2 -kirjasto, mutta ajauduin sen suhteen ongelmiin heti alussa enkä meinannut saada ympyröiden tunnistusta toimimaan, jota tarvitsen silloin kun drone hoveraa mukien yläpuolelle oikeaan kohtaan. Cv2 oli myös hämmästyttävän vaikea saada toimimaan yks yhteen dronen ohjauskirjaston kanssa, joka oli pakollista koska kirjasto kontrolloi pohjakameran käyttöä. Loppujen lopuksi en edes onnistunut siinä määräaikaan mennessä, yhdessä välissä pohjakamera toimi kuten pitikin mutta resetoitui dronen uudelleenkäynnistyksen yhteydessä. Mukien tunnistusparametrien säätöön meni myös paljon aikaa.

Koodia on kovin vähän mutta sitä varten on nähty vaivaa ja se on perusta lopputyölle. Tällä hetkellä koodi tunnistaa mukit ylhäältä päin kuvattuna hyvin ja kohtuullisen harvoin tunnistaa muita ympyrähköjä muotoja (kuva tunnistuksesta löytyy kansiosta documentation/extra). Koodista on helppo poimia esimerkiksi alimman mukin koordinaatit kamerassa ja tehdä tälle logiikka missä kohtaa pongipallo tiputetaan. Päädyin ratkaisuun tehdä dronen taakse avonaisen rautalankaviritelmän josta pallo tippuu kun drone tekee backflipin - se tapahtuu melkoisen äkäisellä nopeudella ja toimii melko varmasti. Kun saan tiputuksen toimimaan ja kohdistuksen suunnilleen oikein, drone tekee käytännössä jo sille määritellyt vähimmäisvaatimukset.

Periaatteessa pythonia varten olisi mahdollista tehdä testejä ja esimerkiksi pallon tiputtajalle olisi mahdollista tehdä testejä joissa cv2 -videonkäsittelijälle annettaisiin kuvia, mutta en koe että siitä olisi lainkaan merkittävää hyötyä. Ajattelin hyödyntää testauksessa pelkkää käytännön testausta. Noh. Katsotaan nyt kuinka monimutkainen tästä kehittyy.

Seuraava tavoite on saada ensi deadlineen mennessä vähintäänkin logiikka joka tiputtaa pallon onnistuneesti, mutta toivottavasti ja luultavasti jotain muutakin.

Käytetyt tunnit: 7h
