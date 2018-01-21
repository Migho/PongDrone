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

## Viikkoraportti 4 (9.1)

Havaintoja:

- Drone ei pysy paikallaan
- Pieni huone on huono testaukselle
- Ulkona ei tätä sovellusta voi käyttää koska tuuli haittaa tarkkuutta
- Flipin yhteydessä drone nostaa reippaasti korkeutta noin metrin
- Drone ei tiedosta hyvin korkeuttaan
- Akku on huono
- Akku kestää ladata
- 70% liikkuminen 0.1 sekunnin ajan on itse asiassa aika paljon.

Mjooh. Nyt on viimeistään selvää että drone tulee osumaan mukiin ehkä 5% todennäköisyydellä (mikä tosin on varmaan silti enemmän kuin average klusteripelaaja). Voltin yhteydessä drone tekee pakonomaisen hervottoman nousun ja dronea on muutenkin mahdoton pitää paikallaan. Noh, olipahan hauska idea.

On kovin harmillista että toinen akku ei toimi, sillä akun lataaminen on hidasta eikä akku jaksa kovin pitkään lentoa. Olen yrittänyt saada tänään dronea pysymään paikoillaan mukin yläpuolella mutta se on vaikeaa, lisäksi mukintunnistus olettaa kovin helposti lattiaan heijastuvan valaisinympyrän olevan muki johon tähdätä. Extra-kansiossa on video dronen lennosta. Tuon videon kuvaamisen aikoihin drone siis lenti mukin suuntaan 100% vauhdilla jos ympyrän keskipiste oli ruudun reunalla ja vastaavasti 0% jos keskellä. Se on liikaa sillä esimerkiksi 70% vauhti ei juuri liikuta dronea välittömästi mutta saa aikaan heijauksen. Muutin arvoja siten että nopeus onkin vain puolet aiemmasta mutten saanut kaapattua määräaikaan mennessä uutta videota sen toiminnasta.

Seuraavaksi hienosäädän dronen pysymään mahdollisimman hyvin paikallaan mukin yläpuolella, ja lisään droneen kontrollit. Alkuperäinen pyrkimys siis oli että drone itse likkuisi mukien yläpuolelle mutta dronen siirtäminen sinne itse on huomattavasti helpompaa, ja koska kurssi lähenee loppuaan on mielestäni järkevämpää tehdä ensin vähän ominaisuuksia sisältävä ohjelma kuin käyttökelvoton ohjelma. Eli kontrolleilla drone ohjattaisiin mukin yläpuolelle ja sen jälkeen autopilotti ottaa ohjat, ja myöhemmin pyrittäisiin korvaamaan koko manuaalinen ohjaus.

Käytetyt tunnit: 6h

## Viikkoraportti 5 (15.1)

Droneen on toteutettu nyt omat kontrollit, ja ne ovat kiusallisesti samassa tiedostossa kuin muukin sälä. Sen siirtoa voisi ehkä miettiä, mutta loppujen lopuksi koodia tuskin tulee enää mahdottomasti. Tällä viikolla samat ongelmat vaivasivat kuin viimeksikin, testaus on hankalaa ja hidasta. Manuaalikontrollit helpottavat toteutusta hieman, sillä nyt mukia ei tarvitse enää käsin siirtää vaan dronen karatessa muualle voin ottaa manuaalikontrollit käyttöön ja siirtää dronen niiden avulla takaisin mukin yläpuolelle.

Tein muutoksia dronen älyyn liikkua mukin sijainnin mukaan mutta se on edelleen kovin surkea. Todennäköisesti koko ensi viikko menee sen hienosäätöön, ilmeisesti pitäisi huomioida samaan aikaan sekä dronen paikallaan pysymättömyys että mukin katoaminen näkökentästä jotenkin, vaikeaksi menee. Tälläkin viikolla loppuunkulutettu akku ja mahdottoman pitkä latausaika olivat ikäviä ongelmia.

Käytetyt tunnit: 5h

## LOPPUPALAUTUS (21.1)

Vaihdoin dronen toimintaa melko paljon. Aiemmin drone liikkui tietyn ajan nopeudella joka laskettiin etäisyydestä. Nyt drone liikkuu tietyn ajan etäisyyden mukaan ja nopeus on fixed. Tarkoituksena on ettei drone heijaa itseään liian kauas liian helposti. Lisäksi dronella on nyt tähtäinalue, ja kun muki pysyy alueella tarpeeksi pitkään, voltti tapahtuu.

Itse asiassa koodi piti saada valmiiksi jo ennen viikonloppua, mutta en onnistunut siinä. Viikonlopun olen ollut landella jonka vuoksi en ole taas voinut testata koodia, joten suurin osa koodista on tehty ilman testausta. Loppujen lopuksi en koe tätä itse asiassa edes kovin pahana, sillä testaus on todella turhauttavaa ja hidasta vajaan 10 minuuttia kestävällä akulla, jonka lataus kestää 1,5h. Tbh mieluummin teenkin koodin ensin valmiiksi ja testaan lopuksi yhden illan aikana hienosäätämällä eri parametreja.

Koska koodia ei siis ole loppupalautukseen kunnolla testattu, aion todennäköisesti hioa eri parametreja vielä ennen demotilaisuutta. Kyseiset muuttujat löytyvät selkeästi koodista eikä ydinkoodia tai kaavoja tarvitse muuttaa sitä varten, joten mielestäni nykyinen koodi on kelpuutettavissa arvosteluun. Koska drone on kovin herkkä lähtemään omille teilleen, olen ehkä hieman skeptinen siitä miten hyvin saan dronen toimimaan demotilaisuudessa, mutta katsotaan miten käy. Joka tapauksessa kurssi oli opettavainen ja mielenkiintoinen.

Käytetyt tunnit: 6h
